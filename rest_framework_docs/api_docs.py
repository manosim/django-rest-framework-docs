from operator import attrgetter
from importlib import import_module
from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from django.utils.module_loading import import_string
from rest_framework.views import APIView
from rest_framework_docs import SERIALIZER_FIELDS
from rest_framework_docs.api_endpoint import ApiEndpoint


class ApiDocumentation(object):

    def __init__(self, drf_router=None, filter_param=None):
        """
        :param filter_param: namespace or app_name
        """
        SERIALIZER_FIELDS.clear()
        self.endpoints = []
        self.drf_router = drf_router
        try:
            root_urlconf = import_string(settings.ROOT_URLCONF)
        except ImportError:
            # Handle a case when there's no dot in ROOT_URLCONF
            root_urlconf = import_module(settings.ROOT_URLCONF)
        if hasattr(root_urlconf, 'urls'):
            self.get_all_view_names(root_urlconf.urls.urlpatterns, filter_param=filter_param)
        else:
            self.get_all_view_names(root_urlconf.urlpatterns, filter_param=filter_param)

    def get_all_view_names(self, urlpatterns, parent_pattern=None, filter_param=None):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver) and (not filter_param or filter_param in [pattern.app_name, pattern.namespace]):
                # parent_pattern = None if pattern._regex == "^" else pattern
                self.get_all_view_names(urlpatterns=pattern.url_patterns, parent_pattern=None if pattern._regex == "^" else pattern, filter_param=filter_param)
            elif isinstance(pattern, RegexURLPattern) and self._is_drf_view(pattern) and not self._is_format_endpoint(pattern):
                if not filter_param or parent_pattern:
                    api_endpoint = ApiEndpoint(pattern, parent_pattern, self.drf_router)
                    self.endpoints.append(api_endpoint)

    def _is_drf_view(self, pattern):
        """
        Should check whether a pattern inherits from DRF's APIView
        """
        return hasattr(pattern.callback, 'cls') and issubclass(pattern.callback.cls, APIView)

    def _is_format_endpoint(self, pattern):
        """
        Exclude endpoints with a "format" parameter
        """
        return '?P<format>' in pattern._regex

    def get_endpoints(self):
        return sorted(self.endpoints, key=attrgetter('name', 'path'))
