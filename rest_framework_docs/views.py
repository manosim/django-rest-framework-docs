from django.http import Http404
from django.views.generic.base import TemplateView
from rest_framework_docs.api_docs import ApiDocumentation
from rest_framework_docs.settings import DRFSettings


class DRFDocsView(TemplateView):

    template_name = "rest_framework_docs/home.html"

    def get_context_data(self, **kwargs):
        settings = DRFSettings().settings
        search_query = self.request.GET.get("search", "")
        filter_param = self.kwargs.get("filter_param", None)

        if settings["HIDE_DOCS"]:
            raise Http404("Django Rest Framework Docs are hidden. Check your settings.")

        docs = ApiDocumentation(filter_param=filter_param)
        endpoints = docs.get_endpoints()

        if filter_param and not endpoints:
            raise Http404("The are no endpoints for \"%s\"." % filter_param)

        if search_query and endpoints:
            endpoints = [endpoint for endpoint in endpoints if search_query in endpoint.path]

        context = super(DRFDocsView, self).get_context_data(**kwargs)
        context['query'] = search_query
        context['endpoints'] = endpoints
        return context
