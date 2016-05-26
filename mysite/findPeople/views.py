from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .forms import GeoLocationForm
from .models import GeoLocation

def viewLocations(request):
    #return HttpResponse("Here are the locations of people")
    location = GeoLocation.objects.first()
    return render_to_response('findPeople/locationPage.html')
    #return render(request, 'findPeople/locationPage.html', {'lat':location.lat, 'lon':location.lon})

def locations(request):
    print(type(request.session._get_or_create_session_key()))
    print(request.session._get_or_create_session_key()) #todo: better to call private method, or create my own session ID?
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            #Always use get on request.POST. Correct way of querying a QueryDict.
            lat = request.POST.get('lat')
            lon = request.POST.get('lon')
            data = {"lat":lat , "lon" : lon}
            
            #create and save a new geolocation with given coords.
            g = GeoLocation(lat=lat, lon=lon)
            g.save()
            
            #Returning same data back to browser
            return JsonResponse(data)
    
    #Get goes here
    # return known locations as json
    locationsDict = dict(locations=list(GeoLocation.objects.values()))
    return JsonResponse(locationsDict)

