from django.contrib.admindocs.views import simplify_regex
from rest_framework.views import APIView


class ApiEndpoint(object):

    def __init__(self, pattern, parent_pattern=None):
        self.pattern = pattern
        self.url_parent_regex = simplify_regex(parent_pattern.regex.pattern)[:-1] if parent_pattern else None
        self.url_regex = ("{0}{1}".format(self.url_parent_regex, simplify_regex(pattern.regex.pattern))) if self.url_parent_regex else simplify_regex(pattern.regex.pattern)
        self.url_name = pattern.name
        self.regex = simplify_regex(pattern._regex)
        self.view_name = pattern.callback.__name__
        # self._get_api_callback(pattern)

    def _get_api_callback(self, pattern):
        """
        Verifies that pattern callback is a subclass of APIView, and returns the class
        """
        if (hasattr(pattern.callback, 'cls') and issubclass(pattern.callback.cls, APIView)):
            return pattern.callback.cls
