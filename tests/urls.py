from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_docs.urls')),

    # API
    # url(r'^accounts/', view=include('project.accounts.urls', namespace='accounts')),
    # url(r'^organisations/', view=include('project.organisations.urls', namespace='organisations')),
]
