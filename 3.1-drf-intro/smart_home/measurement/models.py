from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)


class Measurement(models.Model):
    id = models.IntegerField
    temperature = models.IntegerField
    created_at = models.DateTimeField
