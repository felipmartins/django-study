from django.shortcuts import render
from accounts.form import CreateUserForm
from accounts.models import User

def index(request):

    if request.method == "POST":
        user_form = CreateUserForm(request.POST)

        if user_form.is_valid():
            user_data = user_form.cleaned_data
            user = User.objects._create_employe(**user_data)

    context = {"user_form": CreateUserForm(), "users": User.objects.all()}
    return render(request, "accounts/index.html", context)
