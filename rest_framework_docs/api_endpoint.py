import json
import inspect

from django.contrib.admindocs.views import simplify_regex
from django.utils.encoding import force_str

from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework_docs import SERIALIZER_FIELDS


VIEWSET_METHODS = {
    'List': ['get', 'post'],
    'Instance': ['get', 'put', 'patch', 'delete'],
}


class ApiEndpoint(object):

    def __init__(self, pattern, parent_pattern=None):
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
        self.nb_recurse = 0
        self.fields = self.__get_serializer_fields__()
        self.fields_json = self.__get_serializer_fields_json__()
        self.permissions = self.__get_permissions_class__()

    def __get_path__(self, parent_pattern):
        if parent_pattern:
            return simplify_regex(parent_pattern.regex.pattern + self.pattern.regex.pattern)
        return simplify_regex(self.pattern.regex.pattern)

    def __get_allowed_methods__(self):
        callback_cls = self.callback.cls

        def is_method_allowed(method_name):
            return hasattr(callback_cls, method_name) or (
                issubclass(callback_cls, ModelViewSet) and
                method_name in VIEWSET_METHODS.get(self.callback.suffix, []))

        return sorted([force_str(name).upper() for name in callback_cls.http_method_names if is_method_allowed(name)])

    def __get_docstring__(self):
        return inspect.getdoc(self.callback)

    def __get_permissions_class__(self):
        for perm_class in self.pattern.callback.cls.permission_classes:
            return perm_class.__name__

    def __get_serializer_fields__(self):
        fields = []

        if hasattr(self.callback.cls, 'serializer_class') and hasattr(self.callback.cls.serializer_class, 'get_fields'):
            serializer = self.callback.cls.serializer_class
            if hasattr(serializer, 'get_fields'):
                try:
                    fields = self.__get_fields__(serializer)
                except KeyError as e:
                    self.errors = e
                    fields = []

                # FIXME:
                # Show more attibutes of `field`?

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
