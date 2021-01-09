from django.db import models

class ManagerDetail(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name