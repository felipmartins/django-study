from django.shortcuts import render, redirect
from groups.forms import CreateGroupForm
from groups.models import Group


def group_index(request):

    context = {"groups": Group.objects.all()}
    return render(request, "groups/index.html", context)


def create_group(request):

    if request.method == "POST":
        group_form = CreateGroupForm(request.POST)

        if group_form.is_valid():
            group_form.save() 
            return redirect('group-index')

    context = {"group_form": CreateGroupForm()}

    return render(request, "groups/create_group.html", context)