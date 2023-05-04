from django.shortcuts import render
from groups.forms import CreateGroupForm


def group_index(request):
    context = {"group_form": CreateGroupForm()}
    return render(request, "groups/index.html", context)