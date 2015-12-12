from django.contrib.admindocs.views import simplify_regex
from rest_framework.views import APIView


class ApiEndpoint(object):

    def __init__(self, pattern):
        self.pattern = pattern
        self.regex = simplify_regex(pattern._regex)
        self.view_name = pattern.callback.__name__
        # self._get_api_callback(pattern)

    def _get_api_callback(self, pattern):
        """
        Verifies that pattern callback is a subclass of APIView, and returns the class
        """
        if (hasattr(pattern.callback, 'cls') and issubclass(pattern.callback.cls, APIView)):
            return pattern.callback.cls
