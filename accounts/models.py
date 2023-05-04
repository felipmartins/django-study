from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):

    def _create_employe(self, username, email, password, **extra_fields):
        user = super._create_user(self, username, email, password, **extra_fields)
        user.is_staff = True
        user.save()
        return user

    def _create_manager(self, username, email, password, **extra_fields):
        user = super._create_user(self, username, email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    
    objects = CustomUserManager()

