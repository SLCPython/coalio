# encoding: utf-8
# managers.py

from django.contrib.auth.models import (
    BaseUserManager,
)

class CoalioUserManager(BaseUserManager):
    def create_user(self, email,
                        password=None):
        if not email:
            msg = "Users must have a valid email address"
            raise ValueError(msg)

        user = self.model(
            email = CoalioUserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,
                            email,
                            password):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(
            email,
            password=password
        )
        user.role = "admin"
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user