from django.contrib import admin
from django.urls import path
from accounts.views import index, create_user

urlpatterns = [
    path('', index, name="index"),
    path('user/new', create_user, name="new-user")
]
