import json
import inspect
from django.contrib.admindocs.views import simplify_regex
from django.utils.encoding import force_str
from rest_framework.serializers import BaseSerializer


class ApiNode(object):

    def __init__(self, pattern, parent_node=None, drf_router=None):
        self.pattern = pattern
        self.parent_node = parent_node
        self.drf_router = drf_router

    @property
    def parent_pattern(self):
        if self.parent_node is None:
            return None
        return self.parent_node.pattern

    @property
    def name_parent(self):
        if self.parent_pattern is None:
            return None
        return simplify_regex(self.parent_pattern.regex.pattern).strip('/')

    @property
    def name_parent_full(self):
        name_parent_full = self.name_parent
        if name_parent_full is None:
            return None
        parent_node = self.parent_node
        parent_name = parent_node.name_parent
        while parent_name is not None:
            name_parent_full = "{}/{}".format(parent_name, name_parent_full)
            parent_node = parent_node.parent_node
            parent_name = parent_node.name_parent
        return name_parent_full

    @property
    def path(self):
        pattern = self.__get_path__(self.parent_pattern)
        if pattern is None:
            return None
        parent = self.parent_node
        name_parent = None if parent is None else parent.name_parent
        while name_parent is not None:
            pattern = "{}/{}".format(name_parent, pattern)
            parent = parent.parent_node
            name_parent = parent.name_parent
        if pattern[0] != "/":
            pattern = "/{}".format(pattern)
        return pattern

    def __get_path__(self, parent_pattern):
        if parent_pattern:
            return "{0}{1}".format(
                self.name_parent,
                simplify_regex(self.pattern.regex.pattern)
            )
        return simplify_regex(self.pattern.regex.pattern)


class ApiEndpoint(ApiNode):

    def __init__(self, pattern, parent_node=None, drf_router=None):
        super(ApiEndpoint, self).__init__(
            pattern,
            parent_node=parent_node,
            drf_router=drf_router
        )
        self.callback = pattern.callback
        self.docstring = self.__get_docstring__()
        self.allowed_methods = self.__get_allowed_methods__()
        self.errors = None
        self.serializer_class = self.__get_serializer_class__()
        if self.serializer_class:
            self.serializer = self.__get_serializer__()
            self.fields = self.__get_serializer_fields__(self.serializer)
            self.fields_json = self.__get_serializer_fields_json__()

        self.permissions = self.__get_permissions_class__()

    def __get_allowed_methods__(self):
        viewset_methods = []
        if self.drf_router:
            for prefix, viewset, basename in self.drf_router.registry:
                if self.callback.cls != viewset:
                    continue

                lookup = self.drf_router.get_lookup_regex(viewset)
                routes = self.drf_router.get_routes(viewset)

                for route in routes:

                    # Only actions which actually exist on the viewset will be bound
                    mapping = self.drf_router.get_method_map(viewset, route.mapping)
                    if not mapping:
                        continue

                    # Build the url pattern
                    regex = route.url.format(
                        prefix=prefix,
                        lookup=lookup,
                        trailing_slash=self.drf_router.trailing_slash
                    )
                    if self.pattern.regex.pattern == regex:
                        funcs, viewset_methods = zip(
                            *[(mapping[m], m.upper()) for m in self.callback.cls.http_method_names if m in mapping]
                        )
                        viewset_methods = list(viewset_methods)
                        if len(set(funcs)) == 1:
                            func_docstring = inspect.getdoc(getattr(self.callback.cls, funcs[0]))
                            if func_docstring is not None:
                                self.docstring = func_docstring
        view_methods = [force_str(m).upper() for m in self.callback.cls.http_method_names if hasattr(self.callback.cls, m)]
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

    def __get_serializer_fields__(self, serializer):
        fields = []

        if hasattr(serializer, 'get_fields'):
            for key, field in serializer.get_fields().items():
                to_many_relation = True if hasattr(field, 'many') else False
                sub_fields = []

                if to_many_relation:
                    sub_fields = self.__get_serializer_fields__(field.child) if isinstance(field, BaseSerializer) else None
                else:
                    sub_fields = self.__get_serializer_fields__(field) if isinstance(field, BaseSerializer) else None

                fields.append({
                    "name": key,
                    "type": str(field.__class__.__name__),
                    "sub_fields": sub_fields,
                    "required": field.required,
                    "to_many_relation": to_many_relation
                })
            # FIXME:
            # Show more attibutes of `field`?

        return fields

    def __get_serializer_fields_json__(self):
        # FIXME:
        # Return JSON or not?
        return json.dumps(self.fields)
