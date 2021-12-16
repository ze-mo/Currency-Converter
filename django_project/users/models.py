from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name