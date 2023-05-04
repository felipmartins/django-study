from django.forms import ModelForm
from accounts.models import User


class CreateUserForm(ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "email"]