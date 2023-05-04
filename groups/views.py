from django.shortcuts import render
from groups.forms import CreateGroupForm
from groups.models import Group


def group_index(request):

    if request.method == "POST":
        group_form = CreateGroupForm(request.POST)

        if group_form.is_valid():
            
            group_form.save() 
            
    context = {"group_form": CreateGroupForm(), "groups": Group.objects.all()}
    return render(request, "groups/index.html", context)