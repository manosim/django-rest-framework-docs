from django.conf.urls import patterns, include, url

from restapi import urls as apiurls
from app import urls as appurls

urlpatterns = apiurls.urlpatterns + appurls.urlpatterns
