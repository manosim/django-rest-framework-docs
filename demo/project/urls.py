"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import django
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_docs.views import DRFDocsView
from .accounts.urls import account_urlpatterns, account_router
from .organisations.urls import organisations_urlpatterns, members_urlpatterns, organisation_router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

# Django 1.9 Support for the app_name argument is deprecated
# https://docs.djangoproject.com/en/1.9/ref/urls/#include
django_version = django.VERSION
if django.VERSION[:2] >= (1, 9, ):
    urlpatterns.extend([
        url(r'^accounts/', view=include(account_urlpatterns, namespace='accounts')),
        url(r'^organisations/', view=include(organisations_urlpatterns, namespace='organisations')),
        url(r'^members/', view=include(members_urlpatterns, namespace='members')),
    ])
else:
    urlpatterns.extend([
        url(r'^accounts/', view=include(account_urlpatterns, namespace='accounts', app_name='account_app')),
        url(r'^organisations/', view=include(organisations_urlpatterns, namespace='organisations', app_name='organisations_app')),
        url(r'^members/', view=include(members_urlpatterns, namespace='members', app_name='organisations_app')),
    ])


routers = [account_router, organisation_router]
urlpatterns.extend([
    url(r'^docs/(?P<filter_param>[\w-]+)/$', DRFDocsView.as_view(drf_router=routers), name='drfdocs-filter'),
    url(r'^docs/$', DRFDocsView.as_view(drf_router=routers), name='drfdocs'),
])
