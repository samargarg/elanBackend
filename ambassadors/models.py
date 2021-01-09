from django.db import models

class AmbassadorDetail(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField
    phone = models.CharField(max_length=10)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)

    # Password to be removed
    password = models.CharField(max_length=45)

    institute = models.CharField(max_length=200)

    def __str__(self):
        return self.name