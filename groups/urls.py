from django.urls import path
from groups.views import group_index, create_group, retrieve_group


urlpatterns = [
    path('', group_index, name="group-index"),
    path('group/new', create_group, name="new-group"),
    path('group/<int:group_id>', retrieve_group, name="group-details"),
]