from django.urls import path, include
from groups.views import group_index, create_group


urlpatterns = [
    path('', group_index, name="group-index"),
    path('group/new', create_group, name="new-group")
]