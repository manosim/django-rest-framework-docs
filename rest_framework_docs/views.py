from django.http import Http404
from django.views.generic.base import TemplateView
from rest_framework_docs.api_docs import ApiDocumentation
from rest_framework_docs.settings import DRFSettings


class DRFDocsView(TemplateView):

    template_name = "rest_framework_docs/home.html"

    def get_context_data(self, **kwargs):
        settings = DRFSettings().settings
        search_query = self.request.GET.get("search", "")
        parent_app = self.kwargs.get("parent_app", None)

        if settings["HIDE_DOCS"]:
            raise Http404("Django Rest Framework Docs are hidden. Check your settings.")

        docs = ApiDocumentation(parent_app=parent_app)
        endpoints = docs.get_endpoints()

        if parent_app and not endpoints:
            raise Http404("The are no endpoints for \"%s\"." % parent_app)

        if search_query and endpoints:
            endpoints = [endpoint for endpoint in endpoints if search_query in endpoint.path]

        context = super(DRFDocsView, self).get_context_data(**kwargs)
        context['query'] = search_query
        context['endpoints'] = endpoints
        return context
