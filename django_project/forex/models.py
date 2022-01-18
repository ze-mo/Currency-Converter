from django.db import models

class ForexTestTable(models.Model):
    last_refresh = models.DateTimeField()
    currency = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.currency