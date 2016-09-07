from __future__ import absolute_import, division, print_function

import django
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from rest_framework_docs.views import DRFDocsView
from tests import views


accounts_urls = [
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^login2/$', views.LoginWithSerilaizerClassView.as_view(), name="login2"),
    url(r'^register/$', views.UserRegistrationView.as_view(), name="register"),
    url(r'^reset-password/$', view=views.PasswordResetView.as_view(), name="reset-password"),
    url(r'^reset-password/confirm/$', views.PasswordResetConfirmView.as_view(), name="reset-password-confirm"),

    url(r'^user/profile/$', views.UserProfileView.as_view(), name="profile"),

    url(r'^test/$', views.TestView.as_view(), name="test-view"),
]

organisations_urls = [
    url(r'^create/$', view=views.CreateOrganisationView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/members/$', view=views.OrganisationMembersView.as_view(), name="members"),
    url(r'^(?P<slug>[\w-]+)/leave/$', view=views.LeaveOrganisationView.as_view(), name="leave"),
    url(r'^(?P<slug>[\w-]+)/errored/$', view=views.OrganisationErroredView.as_view(), name="errored"),
    url(r'^(?P<slug>[\w-]+)/$', view=views.RetrieveOrganisationView.as_view(), name="organisation"),
]

router = SimpleRouter()
router.register('organisation-model-viewsets', views.TestModelViewSet, base_name='organisation')

members_urls = [
    url(r'^(?P<slug>[\w-]+)/members/$', view=views.OrganisationMembersView.as_view(), name="members"),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^docs/(?P<filter_param>[\w-]+)/$', DRFDocsView.as_view(drf_router=router), name='drfdocs-filter'),
    url(r'^docs/$', DRFDocsView.as_view(drf_router=router), name='drfdocs'),

    # API
    # url(r'^accounts/', view=include(accounts_urls, namespace="accounts")),
    # url(r'^organisations/', view=include(organisations_urls, namespace='organisations')),
    url(r'^', include(router.urls)),

    # Endpoints without parents/namespaces
    url(r'^another-login/$', views.LoginView.as_view(), name="login"),
]

# Django 1.9 Support for the app_name argument is deprecated
# https://docs.djangoproject.com/en/1.9/ref/urls/#include
django_version = django.VERSION
if django.VERSION[:2] >= (1, 9, ):
    organisations_urls = (organisations_urls, 'organisations_app', )
    members_urls = (members_urls, 'organisations_app', )
    urlpatterns.extend([
        url(r'^accounts/', view=include(accounts_urls, namespace="accounts")),
        url(r'^organisations/', view=include(organisations_urls, namespace='organisations')),
        url(r'^members/', view=include(members_urls, namespace='members')),
    ])
else:
    urlpatterns.extend([
        url(r'^accounts/', view=include(accounts_urls, namespace="accounts", app_name='accounts_app')),
        url(r'^organisations/', view=include(organisations_urls, namespace='organisations', app_name='organisations_app')),
        url(r'^members/', view=include(members_urls, namespace='members', app_name='organisations_app')),
    ])
