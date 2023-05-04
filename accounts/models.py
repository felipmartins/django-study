from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):

    def _create_employe(self, **fields):
        username = fields.pop("username")
        email = fields.pop("email")
        password = fields.pop("password")
        user = super()._create_user(username, email, password, **fields)
        user.is_staff = True
        user.save()
        return user

    def _create_manager(self, **fields):
        username = fields.pop("username")
        email = fields.pop("email")
        password = fields.pop("password")
        user = super()._create_user(username, email, password, **fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):

    objects = CustomUserManager()

