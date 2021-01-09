from django.db import models
from managers.models import *
from ambassadors.models import *
from django.contrib.auth.models import User

class Task(models.Model):
    serial = models.IntegerField
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    assigner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="tasks_assigned_by_me")
    assignee = models.ForeignKey(User, on_delete=models.PROTECT, related_name="tasks_assigned_to_me")
    completed = models.BooleanField
    points = models.IntegerField

    def __str__(self):
        return self.title