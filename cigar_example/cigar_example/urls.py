from django.conf.urls import patterns, include

urlpatterns = patterns('',
    (r'', include('cigar_example.restapi.urls')),
    (r'', include('cigar_example.app.urls')),
)
