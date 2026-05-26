

from django.db import models
from .city import City
from simple_history.models import HistoricalRecords

class Company(models.Model):

    name = models.CharField(max_length=255)

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="companies"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.name