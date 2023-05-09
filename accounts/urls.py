from django.contrib import admin
from django.urls import path
from accounts.views import index, create_user
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index, name="index"),
    path('user/new', create_user, name="new-user"),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),

]
