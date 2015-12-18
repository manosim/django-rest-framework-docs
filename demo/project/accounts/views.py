from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from rest_framework import parsers, renderers, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from project.accounts.models import User
from project.accounts.serializers import (
    UserRegistrationSerializer, UserProfileSerializer, ResetPasswordSerializer
)


class TestView(TemplateView):
    """
    This view should not be included in DRF Docs.
    """
    template_name = "a_test.html"


class LoginView(APIView):
    """
    A view that allows users to login providing their username and password.
    """

    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserRegistrationView(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    An endpoint for users to view and update their profile information.
    """

    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class PasswordResetView(APIView):

    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def get_object(self):
        email = self.request.data.get('email')
        obj = get_object_or_404(self.queryset, email=email)
        return obj

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        user.send_reset_password_email()
        return Response({}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg": "Password updated successfully."}, status=status.HTTP_200_OK)
