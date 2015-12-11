from django.conf.urls import url
from drfrocs.views import DRFDocsView

urlpatterns = [
    # Url to view the API Docs
    url(r'^docs/$', DRFDocsView.as_view(), name='drfdocs'),
]
