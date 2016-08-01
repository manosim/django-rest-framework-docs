import django
from django.conf.urls import url
from project.accounts import views

from rest_framework.routers import SimpleRouter

account_router = SimpleRouter()
account_router.register('user-model-viewsets', views.UserModelViewset, base_name='account')

account_urlpatterns = [
    url(r'^test/$', views.TestView.as_view(), name="test-view"),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^register/$', views.UserRegistrationView.as_view(), name="register"),
    url(r'^reset-password/$', view=views.PasswordResetView.as_view(), name="reset-password"),
    url(r'^reset-password/confirm/$', views.PasswordResetConfirmView.as_view(), name="reset-password-confirm"),
    url(r'^user/profile/$', views.UserProfileView.as_view(), name="profile"),
] + account_router.urls

# Django 1.9 Support for the app_name argument is deprecated
# https://docs.djangoproject.com/en/1.9/ref/urls/#include
django_version = django.VERSION
if django.VERSION[:2] >= (1, 9, ):
    account_urlpatterns = (account_urlpatterns, 'accounts', )
