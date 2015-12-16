import uuid
from django.db import models
from project.accounts.models import User


class Organisation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    members = models.ManyToManyField(User, through='Membership', through_fields=('organisation', 'user'))

    is_active = models.BooleanField(default=False)


class Membership(models.Model):

    class Meta:
        unique_together = ("organisation", "user")

    MEMBER_ROLES = (
        ("ADMIN", "Admin"),
        ("USER", "User")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    joined = models.DateTimeField(auto_now_add=True)

    organisation = models.ForeignKey(Organisation)
    user = models.ForeignKey(User)
    role = models.CharField(choices=MEMBER_ROLES, max_length=20, default="USER")
    is_owner = models.BooleanField(default=False)
