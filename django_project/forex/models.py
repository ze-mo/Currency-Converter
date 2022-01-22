import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class RatesByPairsModel(DjangoCassandraModel):
    class Meta:
        get_pk_field = 'id'

    pair = columns.Text(primary_key=True, required=True)
    id = columns.TimeUUID(primary_key=True)
    exchange_rate = columns.Float()
    last_refresh = columns.DateTime()