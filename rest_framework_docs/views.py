from django.views.generic.base import TemplateView
from rest_framework_docs.api_docs import ApiDocumentation


class DRFDocsView(TemplateView):

    template_name = "rest_framework_docs/home.html"

    def get_context_data(self, **kwargs):
        context = super(DRFDocsView, self).get_context_data(**kwargs)
        docs = ApiDocumentation()
        context['endpoints'] = docs.get_endpoints()
        return context
