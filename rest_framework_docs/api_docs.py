from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from rest_framework.views import APIView
from rest_framework_docs.api_endpoint import ApiEndpoint


class ApiDocumentation(object):

    def __init__(self):
        self.endpoints = []
        root_urlconf = __import__(settings.ROOT_URLCONF)
        if hasattr(root_urlconf, 'urls'):
            self.get_all_view_names(root_urlconf.urls.urlpatterns)
        else:
            self.get_all_view_names(root_urlconf.urlpatterns)

    def get_all_view_names(self, urlpatterns, parent_pattern=None):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver):
                self.get_all_view_names(urlpatterns=pattern.url_patterns, parent_pattern=pattern)
            elif isinstance(pattern, RegexURLPattern) and self._is_drf_view(pattern):
                api_endpoint = ApiEndpoint(pattern, parent_pattern)
                self.endpoints.append(api_endpoint)

    def _is_drf_view(self, pattern):
        # Should check whether a pattern inherits from DRF's APIView
        return hasattr(pattern.callback, 'cls') and issubclass(pattern.callback.cls, APIView)

    def get_endpoints(self):
        return self.endpoints
