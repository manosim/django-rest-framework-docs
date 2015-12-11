from django.views.generic.base import TemplateView


class DRFDocsView(TemplateView):

    template_name = "drfdocs/home.html"

    def get_context_data(self, **kwargs):
        context = super(DRFDocsView, self).get_context_data(**kwargs)
        context['example'] = True
        return context
