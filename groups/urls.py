from django.urls import path, include
from groups.views import group_index


urlpatterns = [
    path('', group_index)
]