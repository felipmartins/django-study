from django import forms
from django.db import models
from accounts.models import User


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(label="Senha", widget=forms.PasswordInput())
    

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "email"]

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].required = True
        self.fields["email"].required = True
        self.fields["password"].required = True