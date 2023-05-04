from django.shortcuts import render
from accounts.form import CreateUserForm

def index(request):
    context = {"user_form": CreateUserForm()}
    return render(request, "index.html", context)
