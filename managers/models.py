from django.db import models
from django.contrib.auth.models import User

class ManagerDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="manager_detail")
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name