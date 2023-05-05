from django.urls import path
from groups.views import group_index, create_group, retrieve_group


urlpatterns = [
    path('', group_index, name="group-index"),
    path('/new', create_group, name="new-group"),
    path('/<int:group_id>', retrieve_group, name="group-details"),
]