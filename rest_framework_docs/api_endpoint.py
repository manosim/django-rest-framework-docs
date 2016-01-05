import json
import inspect
from django.contrib.admindocs.views import simplify_regex
from rest_framework.viewsets import ModelViewSet


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
                self.name = '%s (REST)' % self.name_parent
        else:
            self.name_parent = ''
            self.name = ''
        # self.labels = (self.name_parent, self.name, slugify(self.name))
        self.labels = dict(parent=self.name_parent, name=self.name)
        self.path = self.__get_path__(parent_pattern)
        self.allowed_methods = self.__get_allowed_methods__()
        self.errors = None
        self.fields = self.__get_serializer_fields__()
        self.fields_json = self.__get_serializer_fields_json__()
        self.permissions = self.__get_permissions_class__()

    def __get_path__(self, parent_pattern):
        if parent_pattern:
            return simplify_regex(parent_pattern.regex.pattern + self.pattern.regex.pattern)
        return simplify_regex(self.pattern.regex.pattern)

    def __get_allowed_methods__(self):
        return [m.upper() for m in self.callback.cls.http_method_names if hasattr(self.callback.cls, m)]

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
