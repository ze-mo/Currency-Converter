from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"


class RatesHistory(models.Model):
    profile_id = models.IntegerField()
    pair = models.CharField(max_length=10, null=True)
    amount = models.FloatField(null=True)
    exchange_rate = models.FloatField(null=True)
    result = models.FloatField(null=True)
    conversion_date = models.DateTimeField()

    class Meta:
        ordering = ['-conversion_date']
