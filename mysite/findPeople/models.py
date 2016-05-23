from django.db import models

# Create your models here.

class GeoLocation(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
         return "Lat: %f, Lon: %f" % (self.lat, self.lon)

