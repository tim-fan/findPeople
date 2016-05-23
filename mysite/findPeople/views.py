from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .forms import GeoLocationForm
from .models import GeoLocation

def viewLocations(request):
    #return HttpResponse("Here are the locations of people")
    location = GeoLocation.objects.first()
    return render(request, 'findPeople/locationPage.html', {'lat':location.lat, 'lon':location.lon})

def sendLocation(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GeoLocationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            #remove all old locations
            GeoLocation.objects.all().delete()
            
            #save the new location
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/findPeople/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GeoLocationForm()

    return render(request, 'findPeople/geoLocation.html', {'form': form})

def getLocations(request):
    # return know locations as json
    locationsDict = dict(locations=list(GeoLocation.objects.values()))
    return JsonResponse(locationsDict)

