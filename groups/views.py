from django.shortcuts import render


def group_index(request):
    return render(request, "groups/index.html")