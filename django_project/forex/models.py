import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from django.db import models
from viewflow.fields import CompositeKey

"""class RatesByPairs(DjangoCassandraModel):
    class Meta:
        get_pk_field = 'id'

    pair = columns.Text(primary_key=True, required=True)
    last_refreshed = columns.DateTime(primary_key=True, required=True)
    exchange_rate = columns.Float()
    id = columns.TimeUUID(primary_key=True)

    def __str__(self):
        return self.pair"""

class RatesByPairs(models.Model):
    pair = models.CharField(primary_key=True, max_length=10)
    last_refreshed = models.DateTimeField()
    exchange_rate = models.FloatField(null=True)