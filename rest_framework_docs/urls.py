from django.conf.urls import url
from rest_framework_docs.views import DRFDocsView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Url to view the API Docs
    url(r'^$', login_required(DRFDocsView.as_view()), name='drfdocs'),
]
