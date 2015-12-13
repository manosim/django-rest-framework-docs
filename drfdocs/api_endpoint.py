from django.contrib.admindocs.views import simplify_regex


class ApiEndpoint(object):

    def __init__(self, pattern, parent_pattern=None):
        self.pattern = pattern
        self.callback = pattern.callback
        self.name = pattern.name
        self.path = self.__get_path__(parent_pattern)
        self.allowed_methods = self.__get_allowed_methods__()
        self.view_name = pattern.callback.__name__
        self.fields = self.__get_serializer_fields__()

    def __get_path__(self, parent_pattern):
        if parent_pattern:
            parent_path = simplify_regex(parent_pattern.regex.pattern)[:-1]
            return "{0}{1}".format(parent_path, simplify_regex(self.pattern.regex.pattern))
        return simplify_regex(self.pattern.regex.pattern)

    def __get_allowed_methods__(self):
        return [m.upper() for m in self.callback.cls.http_method_names if hasattr(self.callback.cls, m)]

    def __get_serializer_fields__(self):
        fields = []

        if hasattr(self.callback.cls, 'serializer_class') and hasattr(self.callback.cls.serializer_class, 'get_fields'):
            serializer = self.callback.cls.serializer_class
            if hasattr(serializer, 'get_fields'):
                fields = [{"name": key, "type": str(value.__class__.__name__)} for key, value in serializer().get_fields().items()]

        return fields
