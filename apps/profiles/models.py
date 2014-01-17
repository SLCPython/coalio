# encoding: utf-8

from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)


class CoalioUser(AbstractBaseUser, PermissionsMixin):
    """
    Default user for uttr profiles.
    Requires email confirmation to activate
    """
    ROLE_CHOICES = (
        ("admin", "Administrator"),
        ("volunteer", "Volunteer"),
        ("peer", "Peer"),
    )

    email = models.EmailField(
        verbose_name=u'email address',
        max_length=255,
        unique=True,
        db_index=True
        )

    first_name = models.CharField(
        max_length=255,
        blank=True
        )
    last_name = models.CharField(
        max_length=255,
        blank=True
        )

    role = models.CharField(
        max_length=7,
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[2][0]
        )

    notes = models.TextField(blank=True)

    USERNAME_FIELD = "email"

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def get_full_name(self):
        # The user is identified by their email and first name
        if self.first_name or self.last_name:
            return "%s (%s %s)" % (self.email, self.first_name, self.last_name)
        else:
            return self.get_short_name()

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

