from django.conf.urls import url, include
from rest_framework import routers
from project.accounts import views


router = routers.DefaultRouter()
router.register(
    r'user_viewset',
    views.UserModelViewSet,
)


urlpatterns = [
    url(r'^test/$', views.TestView.as_view(), name="test-view"),

    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^register/$', views.UserRegistrationView.as_view(), name="register"),
    url(r'^register/$', views.UserRegistrationView.as_view(), name="register"),
    url(r'^reset-password/$', view=views.PasswordResetView.as_view(), name="reset-password"),
    url(r'^reset-password/confirm/$', views.PasswordResetConfirmView.as_view(), name="reset-password-confirm"),

    url(r'^user/profile/$', views.UserProfileView.as_view(), name="profile"),

    url(r'^viewset_test/', include(router.urls), name="user_viewset"),
]
