from django import forms
from django.db import models
from groups.models import Group


class CreateGroupForm(forms.ModelForm):
    
    class Meta:
        model = Group
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        self.fields["title"].required = True