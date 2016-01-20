from rest_framework import serializers
from project.accounts.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password',)
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ('is_active',)


class ResetPasswordSerializer(serializers.ModelSerializer):

    id = serializers.CharField()
    token = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'token', 'password',)
        extra_kwargs = {'password': {'write_only': True}}


class NestedSerializer(serializers.Serializer):
    nb_test = serializers.IntegerField(default=0, required=False)
    liste_codes = serializers.ListField(child=serializers.CharField())


class CustomAuthTokenSerializer(AuthTokenSerializer):
    nested = NestedSerializer(many=True)
