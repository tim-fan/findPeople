from django.forms import ModelForm
from .models import GeoLocation

class GeoLocationForm(ModelForm):
    class Meta:
        model = GeoLocation
        fields = ['lat', 'lon']
