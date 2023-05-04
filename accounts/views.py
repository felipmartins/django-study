from django.shortcuts import render
from accounts.forms import CreateUserForm

def index(request):
    context = {"user_form": CreateUserForm()}
    return render(request, "index.html", context)
