
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.viewLocations, name='location view'),
    url(r'^sendLocation/$', views.sendLocation, name='send location view'),
    url(r'^userLocations/$', views.getLocations, name='get locations view'),
]
