from operator import attrgetter

from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from django.utils.module_loading import import_string

from rest_framework.views import APIView
from rest_framework_docs import SERIALIZER_FIELDS
from rest_framework_docs.api_endpoint import ApiEndpoint


class ApiDocumentation(object):

    def __init__(self, filter_param=None):
        """
        :param filter_param: namespace or app_name
        """
        SERIALIZER_FIELDS.clear()
        self.endpoints = []
        root_urlconf = import_string(settings.ROOT_URLCONF)
        if hasattr(root_urlconf, 'urls'):
            self.get_all_view_names(root_urlconf.urls.urlpatterns, filter_param=filter_param)
        else:
            self.get_all_view_names(root_urlconf.urlpatterns, filter_param=filter_param)

    def get_all_view_names(self, urlpatterns, parent_pattern=None, filter_param=None):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver) and (not filter_param or filter_param in [pattern.app_name, pattern.namespace]):
                self.get_all_view_names(urlpatterns=pattern.url_patterns, parent_pattern=pattern, filter_param=filter_param)
            elif isinstance(pattern, RegexURLPattern) and self._is_drf_view(pattern):
                if not filter_param or (parent_pattern and filter_param in [parent_pattern.app_name, parent_pattern.namespace]):
                    api_endpoint = ApiEndpoint(pattern, parent_pattern)
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
