from rest_framework import serializers
from project.organisations.models import Organisation, Membership
from project.accounts.serializers import UserProfileSerializer


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('joined', 'is_owner', 'role')


class CreateOrganisationSerializer(serializers.ModelSerializer):
    membership_set = MembershipSerializer(many=True)

    class Meta:
        model = Organisation
        fields = ('name', 'slug', 'membership_set')


class OrganisationMembersSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Membership
        fields = ('joined', 'user', 'is_owner', 'role')

    def get_user(self, obj):
        serializer = UserProfileSerializer(obj.user)
        return serializer.data


class OrganisationDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = ('name', 'slug', 'is_active')


class RetrieveOrganisationSerializer(serializers.ModelSerializer):
    membership_set = MembershipSerializer()

    class Meta:
        model = Organisation
        fields = ('name', 'slug', 'is_active', 'membership_set')
