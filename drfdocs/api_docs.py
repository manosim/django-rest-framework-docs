from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from drfdocs.api_endpoint import ApiEndpoint


class ApiDocumentation(object):
    excluded_apps = ["admin", "drfdocs"]
    excluded_endpoints = ["serve"]

    def __init__(self):
        self.endpoints = []
        root_urlconf = __import__(settings.ROOT_URLCONF)
        self.get_all_view_names(root_urlconf.urls.urlpatterns)

    def get_all_view_names(self, urlpatterns, parent_pattern=None):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver) and (pattern.app_name not in self.excluded_apps):
                self.get_all_view_names(urlpatterns=pattern.url_patterns, parent_pattern=pattern)
            elif isinstance(pattern, RegexURLPattern) and (pattern.callback.__name__ not in self.excluded_endpoints):
                api_endpoint = ApiEndpoint(pattern, parent_pattern)
                self.endpoints.append(api_endpoint)

    def _filter_drf_views(self, endpoints):
        # Should keep only the endpoints with views that inherit from DRF's APIView
        pass

    def get_endpoints(self):
        return self.endpoints
