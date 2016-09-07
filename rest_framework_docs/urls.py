from django.conf.urls import url

from rest_framework_docs.settings import DRFSettings
from rest_framework_docs.views import DRFDocsView


settings = DRFSettings().settings
if settings["LOGIN_REQUIRED"]:
    from django.contrib.auth.decorators import login_required
    docs_view = login_required(DRFDocsView.as_view())
else:
    docs_view = DRFDocsView.as_view()

urlpatterns = [
    # Url to view the API Docs
    url(r'^$', docs_view, name='drfdocs'),
    # Url to view the API Docs with a specific namespace or app_name
    url(r'^(?P<filter_param>[\w-]+)/$', docs_view, name='drfdocs-filter'),
]
