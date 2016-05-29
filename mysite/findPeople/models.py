from django.db import models

# Create your models here.

class LocationObservation(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
         return "Lat: {lat}, Lon: {lon}, Time: {time}".format(
            lat = self.lat,
            lon = self.lon,
            time = self.time)
         
class User(models.Model):
    #TODO: userIDs are unique?
    userId = models.UUIDField()
    lastSeenLocation = models.OneToOneField(LocationObservation)

