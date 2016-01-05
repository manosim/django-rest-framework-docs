from django.conf.urls import url
from rest_framework_docs.views import DRFDocsView

urlpatterns = [
    # Url to view the API Docs
    url(r'^$', DRFDocsView.as_view(), name='drfdocs'),
    # Url to view the API Docs with a specific namespace or app_name
    url(r'^(?P<filter_param>[\w-]+)/$', DRFDocsView.as_view(), name='drfdocs-filter'),
]
