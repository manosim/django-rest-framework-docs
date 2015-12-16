from django.conf.urls import include, url
from django.contrib import admin
from tests import views

accounts_urls = [
    url(r'^login/$', views.LoginView.as_view(), name="login"),
]

organisations_urls = [

]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_docs.urls')),

    # API
    url(r'^accounts/', view=include(accounts_urls, namespace='accounts')),
    url(r'^organisations/', view=include(organisations_urls, namespace='organisations')),
]
