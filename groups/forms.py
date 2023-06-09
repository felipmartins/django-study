from django import forms
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from groups.models import Group
from accounts.models import User


class CreateGroupForm(forms.ModelForm):

    class Media:
        css = {
            "all": ('/static/admin/css/widgets.css',)
        }
        js = ("/admin/jsi18n",)

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=FilteredSelectMultiple("Pessoas usuárias", False),
        required = True
    )


    class Meta:
        model = Group
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        self.fields["title"].required = True
        self.fields["title"].label = "Nome do Grupo"
        self.fields["users"].label = ""



class UpdateUsersGroupForm(forms.ModelForm):

    class Media:
        css = {
            "all": ('/static/admin/css/widgets.css',)
        }
        js = ("/admin/jsi18n",)

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=FilteredSelectMultiple("Pessoas usuárias", False),
        required = True
    )


    class Meta:
        model = Group
        fields = ["users"]

    def __init__(self, group_id=None, *args, **kwargs):
        super(UpdateUsersGroupForm, self).__init__(*args, **kwargs)
        group = Group.objects.get(id=group_id)
        self.fields["users"].initial = group.users.all()
        self.fields["users"].label = ""
        