from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern


class ApiDocumentation(object):
    excluded_apps = ["admin", "drfdocs"]
    excluded_endpoints = ["serve"]
    root_urlconf = __import__(settings.ROOT_URLCONF)

    def __init__(self):
        self.view_names = []
        self.get_all_view_names(self.root_urlconf.urls.urlpatterns)

    def get_all_view_names(self, urlpatterns):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver) and (pattern.app_name not in self.excluded_apps):
                self.get_all_view_names(pattern.url_patterns)
            elif isinstance(pattern, RegexURLPattern) and (pattern.callback.__name__ not in self.excluded_endpoints):
                self.view_names.append(pattern.callback.__name__)

    def get_views(self):
        return self.view_names
