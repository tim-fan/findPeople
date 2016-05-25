
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.viewLocations, name='location view'),
    url(r'^locations/$', views.locations, name='get/set location data view'),
]
