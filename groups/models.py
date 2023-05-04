from django.db import models
from accounts.models import User


class Group(models.Model):

    title = models.CharField(max_length=150)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.title} - {self.users.all()}"