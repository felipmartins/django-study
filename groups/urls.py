from django.urls import path
from groups.views import group_index, create_group, retrieve_group, update_group_users


urlpatterns = [
    path('', group_index, name="group-index"),
    path('new', create_group, name="new-group"),
    path('<int:group_id>', retrieve_group, name="group-details"),
    path('update-users/<int:group_id>', update_group_users, name="update-group"),
]