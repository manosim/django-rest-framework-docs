import django
from django.conf.urls import url
from project.organisations import views

from rest_framework.routers import SimpleRouter
from .views import OrganisationModelViewset

organisation_router = SimpleRouter()
organisation_router.register('organisation-model-viewsets', OrganisationModelViewset, base_name='organisation')

organisations_urlpatterns = [
    url(r'^create/$', view=views.CreateOrganisationView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', view=views.RetrieveOrganisationView.as_view(), name="organisation"),
    url(r'^(?P<slug>[\w-]+)/members/$', view=views.OrganisationMembersView.as_view(), name="members"),
    url(r'^(?P<slug>[\w-]+)/leave/$', view=views.LeaveOrganisationView.as_view(), name="leave")
] + organisation_router.urls

members_urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/members/$', view=views.OrganisationMembersView.as_view(), name="members"),
]

# Django 1.9 Support for the app_name argument is deprecated
# https://docs.djangoproject.com/en/1.9/ref/urls/#include
django_version = django.VERSION
if django.VERSION[:2] >= (1, 9, ):
    organisations_urlpatterns = (organisations_urlpatterns, 'organisations', )
    members_urlpatterns = (members_urlpatterns, 'organisations', )
