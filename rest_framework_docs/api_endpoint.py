import json
import inspect
from django.contrib.admindocs.views import simplify_regex
from django.utils.encoding import force_str
from rest_framework.viewsets import ModelViewSet

VIEWSET_METHODS = {
    'List': ['get', 'post'],
    'Instance': ['get', 'put', 'patch', 'delete'],
}


class ApiEndpoint(object):

    def __init__(self, pattern, parent_pattern=None):
        self.pattern = pattern
        self.callback = pattern.callback
        # self.name = pattern.name
        self.docstring = self.__get_docstring__()
        self.name_parent = simplify_regex(parent_pattern.regex.pattern).strip('/') if parent_pattern else None
        self.path = self.__get_path__(parent_pattern)
        self.allowed_methods = self.__get_allowed_methods__()
        # self.view_name = pattern.callback.__name__
        self.errors = None
        self.fields = self.__get_serializer_fields__()
        self.fields_json = self.__get_serializer_fields_json__()
        self.permissions = self.__get_permissions_class__()

    def __get_path__(self, parent_pattern):
        if parent_pattern:
            return "/{0}{1}".format(self.name_parent, simplify_regex(self.pattern.regex.pattern))
        return simplify_regex(self.pattern.regex.pattern)

    def is_method_allowed(self, method_name, callback_cls):
        return hasattr(callback_cls, method_name) or (
            issubclass(callback_cls, ModelViewSet) and method_name in VIEWSET_METHODS.get(self.callback.suffix, [])
        )

    def __get_allowed_methods__(self):
        callback_cls = self.callback.cls
        return sorted([force_str(name).upper() for name in callback_cls.http_method_names if self.is_method_allowed(name, callback_cls)])

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
                    fields = [{
                        "name": key,
                        "type": str(field.__class__.__name__),
                        "required": field.required
                    } for key, field in serializer().get_fields().items()]
                except KeyError as e:
                    self.errors = e
                    fields = []

                # FIXME:
                # Show more attibutes of `field`?

        return fields

    def __get_serializer_fields_json__(self):
        # FIXME:
        # Return JSON or not?
        return json.dumps(self.fields)
