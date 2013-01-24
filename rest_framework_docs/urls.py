from django.conf.urls import patterns, include, url
from views import documentation

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/?$', documentation, name='api-documentation'),
)
