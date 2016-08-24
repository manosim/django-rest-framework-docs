from django.conf.urls import url, include
from rest_framework import routers
from project.organisations import views


router = routers.DefaultRouter()
router.register(
    r'organisation_viewset',
    views.OrganisationViewSet,
)


urlpatterns = [

    url(r'^create/$', view=views.CreateOrganisationView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', view=views.RetrieveOrganisationView.as_view(), name="organisation"),
    url(r'^(?P<slug>[\w-]+)/members/$', view=views.OrganisationMembersView.as_view(), name="members"),
    url(r'^(?P<slug>[\w-]+)/leave/$', view=views.LeaveOrganisationView.as_view(), name="leave"),

    url(r'^', include(router.urls), name="organisation_viewset"),
]
