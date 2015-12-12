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

    def get_all_view_names(self, urlpatterns):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver) and (pattern.app_name not in self.excluded_apps):
                self.get_all_view_names(pattern.url_patterns)
            elif isinstance(pattern, RegexURLPattern) and (pattern.callback.__name__ not in self.excluded_endpoints):
                api_endpoint = ApiEndpoint(pattern)
                self.endpoints.append(api_endpoint)

    def get_endpoints(self):
        return self.endpoints
