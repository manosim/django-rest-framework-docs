from django.conf import settings
from django.views.generic.base import TemplateView
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern


class DRFDocsView(TemplateView):

    root_urlconf = __import__(settings.ROOT_URLCONF)
    template_name = "drfdocs/home.html"
    VIEW_NAMES = []

    def get_all_view_names(self, urlpatterns):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver):
                self.get_all_view_names(pattern.url_patterns)
            elif isinstance(pattern, RegexURLPattern):
                view_name = pattern.callback.__name__
                self.VIEW_NAMES.append(view_name)
        return self.VIEW_NAMES

    def get_context_data(self, **kwargs):
        self.VIEW_NAMES = []
        context = super(DRFDocsView, self).get_context_data(**kwargs)
        all_urlpatterns = self.root_urlconf.urls.urlpatterns
        context['views'] = self.get_all_view_names(all_urlpatterns)
        return context
