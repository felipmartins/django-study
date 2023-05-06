from django.shortcuts import render, redirect
from groups.forms import CreateGroupForm, UpdateUsersGroupForm
from groups.models import Group
from accounts.models import User


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

def retrieve_group(request, group_id):
    
        context = {"group": Group.objects.get(id=group_id)}
        return render(request, "groups/group_details.html", context)

def update_group_users(request, group_id):    

    if request.method == "POST":
        if "users" in request.POST:
            users = {User.objects.get(id=user) for user in dict(request.POST)['users']}
        else:
            users = set()
        group = Group.objects.get(id=group_id)
        users_before = set(group.users.all())
        print(users_before)
        for user in users:
            group.users.add(user)
        users_to_remove = users_before - users

        for user in users_to_remove:
            group.users.remove(user)
             
        group.save()
        return redirect('group-details', group_id=group_id)
    
    context = {"group_form": UpdateUsersGroupForm(group_id=group_id)}

    return render(request, "groups/update_group_users.html", context)

def delete_group(request, group_id):
    
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect('group-index')