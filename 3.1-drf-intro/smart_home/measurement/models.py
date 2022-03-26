from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    # measurements


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    # sensor_id = models.IntegerField()
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
