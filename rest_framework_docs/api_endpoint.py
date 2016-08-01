import json
import inspect
from django.contrib.admindocs.views import simplify_regex
from django.utils.encoding import force_str
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework_docs import SERIALIZER_FIELDS


class ApiEndpoint(object):

    def __init__(self, pattern, parent_pattern=None, drf_router=None):
        self.drf_router = drf_router or []
        if not isinstance(self.drf_router, (list, tuple)):
            self.drf_router = [self.drf_router]
        self.pattern = pattern
        self.callback = pattern.callback
        self.docstring = self.__get_docstring__()
        if parent_pattern:
            self.name_parent = parent_pattern.namespace or parent_pattern.app_name or \
                simplify_regex(parent_pattern.regex.pattern).replace('/', '-')
            self.name = self.name_parent
            if hasattr(pattern.callback, 'cls') and issubclass(pattern.callback.cls, ModelViewSet):
                self.name = '%s (RESTful)' % self.name_parent
        else:
            self.name_parent = ''
            self.name = ''
        # self.labels = (self.name_parent, self.name, slugify(self.name))
        self.labels = dict(parent=self.name_parent, name=self.name)
        self.path = self.__get_path__(parent_pattern)
        self.allowed_methods = self.__get_allowed_methods__()
        self.errors = None
        self.serializer_class = self.__get_serializer_class__()
        if self.serializer_class:
            self.serializer = self.__get_serializer__()
            self.fields = self.__get_serializer_fields__()
            self.fields_json = self.__get_serializer_fields_json__()
        self.permissions = self.__get_permissions_class__()

    def __get_path__(self, parent_pattern):
        if parent_pattern:
            return simplify_regex(parent_pattern.regex.pattern + self.pattern.regex.pattern)
        return simplify_regex(self.pattern.regex.pattern)

    def __get_allowed_methods__(self):

        viewset_methods = []
        for router in self.drf_router:
            for prefix, viewset, basename in router.registry:
                if self.callback.cls != viewset:
                    continue

                lookup = router.get_lookup_regex(viewset)
                routes = router.get_routes(viewset)

                for route in routes:

                    # Only actions which actually exist on the viewset will be bound
                    mapping = router.get_method_map(viewset, route.mapping)
                    if not mapping:
                        continue

                    # Build the url pattern
                    regex = route.url.format(
                        prefix=prefix,
                        lookup=lookup,
                        trailing_slash=router.trailing_slash
                    )
                    if self.pattern.regex.pattern == regex:
                        funcs, viewset_methods = zip(
                            *[(mapping[m], m.upper()) for m in self.callback.cls.http_method_names if m in mapping]
                        )
                        viewset_methods = list(viewset_methods)
                        if len(set(funcs)) == 1:
                            self.docstring = inspect.getdoc(getattr(self.callback.cls, funcs[0]))

        view_methods = [force_str(m).upper() for m in self.callback.cls.http_method_names if
                        hasattr(self.callback.cls, m)]
        return viewset_methods + view_methods

    def __get_docstring__(self):
        return inspect.getdoc(self.callback)

    def __get_permissions_class__(self):
        for perm_class in self.pattern.callback.cls.permission_classes:
            return perm_class.__name__

    def __get_serializer__(self):
        try:
            return self.serializer_class()
        except KeyError as e:
            self.errors = e

    def __get_serializer_class__(self):
        if hasattr(self.callback.cls, 'serializer_class'):
            return self.callback.cls.serializer_class

        if hasattr(self.callback.cls, 'get_serializer_class'):
            return self.callback.cls.get_serializer_class(self.pattern.callback.cls())

    def __get_serializer_fields__(self):
        fields = []
        serializer = None

        if hasattr(self.callback.cls, 'serializer_class'):
            serializer = self.callback.cls.serializer_class

        elif hasattr(self.callback.cls, 'get_serializer_class'):
            serializer = self.callback.cls.get_serializer_class(self.pattern.callback.cls())

        if hasattr(serializer, 'get_fields'):
            try:
                fields = self.__get_fields__(serializer)
            except KeyError as e:
                self.errors = e
                fields = []

        return fields

    def __get_fields__(self, serializer):
        if serializer in SERIALIZER_FIELDS:
            return SERIALIZER_FIELDS.get(serializer)

        fields = []
        for key, field in serializer().get_fields().items():
            item = dict(
                name=key,
                type=str(field.__class__.__name__),
                required=field.required
            )

            # Nested/List serializer
            if isinstance(field, (serializers.ListSerializer, serializers.ListField)):
                sub_type = field.child.__class__
                item['sub_type'] = str(sub_type.__name__)
                if isinstance(sub_type(), serializers.Serializer):
                    item['fields'] = self.__get_fields__(sub_type)
            elif isinstance(field, serializers.Serializer):
                item['fields'] = self.__get_fields__(field.__class__)
            fields.append(item)

        # Keep a copy of serializer fields for optimization purposes
        SERIALIZER_FIELDS[serializer] = fields
        return fields

    def __get_serializer_fields_json__(self):
        # FIXME:
        # Return JSON or not?
        return json.dumps(self.fields)
