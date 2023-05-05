from django import forms
from django.db import models
from accounts.models import User


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(label="Senha", widget=forms.PasswordInput())
    user_type = forms.CharField(max_length=50, widget=forms.Select(choices=[("Liderança", "Liderança"),("Colaboradora", "Colaboradora")]))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "email"]

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].required = True
        self.fields["username"].help_text = ""
        self.fields["email"].required = True
        self.fields["password"].required = True
        self.fields["user_type"].label = "Cargo"        
        self.fields["user_type"].required = True