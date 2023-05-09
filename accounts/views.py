from django.shortcuts import render, redirect
from accounts.form import CreateUserForm
from accounts.models import User
from django.contrib.auth.decorators import login_required



@login_required()
def index(request):

    context = {"users": User.objects.all()}
    return render(request, "accounts/index.html", context)


@login_required
def create_user(request):

    if request.method== "POST":
        user_form = CreateUserForm(request.POST)

        if user_form.is_valid():
            user_data = user_form.cleaned_data
            user_type = user_data.pop("user_type")
            if user_type == "Colaboradora":
                User.objects._create_employe(**user_data)
            else:
                User.objects._create_manager(**user_data)    
        return redirect("index")
    
    context = {"user_form": CreateUserForm()}

    return render(request, "accounts/create_user.html", context)