from django.views.generic.base import TemplateView
from drfdocs.api_docs import ApiDocumentation


class DRFDocsView(TemplateView):

    template_name = "drfdocs/home.html"

    def get_context_data(self, **kwargs):
        context = super(DRFDocsView, self).get_context_data(**kwargs)
        docs = ApiDocumentation()
        context['views'] = docs.get_views()
        return context
