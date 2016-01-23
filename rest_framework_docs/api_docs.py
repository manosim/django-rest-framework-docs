from operator import attrgetter
from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from rest_framework.views import APIView
from rest_framework_docs.api_endpoint import ApiEndpoint


class ApiDocumentation(object):

    def __init__(self, filter_app=None):
        """
        :param filter_app: namespace or app_name
        """
        self.endpoints = []
        root_urlconf = __import__(settings.ROOT_URLCONF)
        if hasattr(root_urlconf, 'urls'):
            self.get_all_view_names(root_urlconf.urls.urlpatterns, filter_app=filter_app)
        else:
            self.get_all_view_names(root_urlconf.urlpatterns, filter_app=filter_app)

    def get_all_view_names(self, urlpatterns, parent_pattern=None, filter_app=None):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver) and (not filter_app or filter_app in [pattern.app_name, pattern.namespace]):
                self.get_all_view_names(urlpatterns=pattern.url_patterns, parent_pattern=pattern, filter_app=filter_app)
            elif isinstance(pattern, RegexURLPattern) and self._is_drf_view(pattern):
                if not filter_app or (parent_pattern and filter_app in [parent_pattern.app_name, parent_pattern.namespace]):
                    api_endpoint = ApiEndpoint(pattern, parent_pattern)
                    self.endpoints.append(api_endpoint)

    def _is_drf_view(self, pattern):
        """
        Should check whether a pattern inherits from DRF's APIView
        """
        return hasattr(pattern.callback, 'cls') and issubclass(pattern.callback.cls, APIView)

    def get_endpoints(self):
        """
        Returns the endpoints sorted by the app name
        """
        return sorted(self.endpoints, key=attrgetter('name'))
