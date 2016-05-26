from django.db import models

# Create your models here.

class GeoLocation(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
         return "Lat: %f, Lon: %f" % (self.lat, self.lon)

class LocationObservation(models.Model):
    location = GeoLocation()
    observationTime = models.DateTimeField()

    def __str__(self):
         return str(self.location) + ", Time: " + str(self.observationTime)
         
class User(models.Model):
    userId = models.UUIDField()
    lastSeenLocation = LocationObservation()

