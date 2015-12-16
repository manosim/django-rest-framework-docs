from django.contrib.admindocs.views import simplify_regex


class ApiEndpoint(object):

    def __init__(self, pattern, parent_pattern=None):
        self.pattern = pattern
        self.callback = pattern.callback
        # self.name = pattern.name
        self.name_parent = simplify_regex(parent_pattern.regex.pattern).replace('/', '') if parent_pattern else None
        self.path = self.__get_path__(parent_pattern)
        self.allowed_methods = self.__get_allowed_methods__()
        # self.view_name = pattern.callback.__name__
        self.errors = None
        self.fields = self.__get_serializer_fields__()

    def __get_path__(self, parent_pattern):
        if parent_pattern:
            return "/{0}{1}".format(self.name_parent, simplify_regex(self.pattern.regex.pattern))
        return simplify_regex(self.pattern.regex.pattern)

    def __get_allowed_methods__(self):
        return [m.upper() for m in self.callback.cls.http_method_names if hasattr(self.callback.cls, m)]

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
