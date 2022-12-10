from datetime import date

from django.db import models


class Currency(models.Model):
    type = models.CharField(max_length=30, null=False)
    value = models.FloatField(null=False)
    date = models.DateField(default=date.today, null=False)
