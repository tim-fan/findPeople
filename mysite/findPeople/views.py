from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.forms.models import model_to_dict

from django.utils import timezone
from uuid import uuid4 as uuid
from uuid import UUID

from .models import LocationObservation, User

def viewLocations(request):
    return render(request, 'findPeople/locationPage.html')

@ensure_csrf_cookie
def locations(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            #Always use get on request.POST. Correct way of querying a QueryDict.
            lat = request.POST.get('lat')
            lon = request.POST.get('lon')
            currentTime = timezone.now()
            
            #create and save a new geolocation with given coords.
            loc = LocationObservation(lat=lat, lon=lon, time = currentTime)
            loc.save()

            session = request.session #TODO: check user cookies enabled
            if not 'id' in session.keys():
                print('newUser')
                userId = uuid()
                session['id'] = str(userId)
            else:
                userId = UUID(session['id'])

            usr, created = User.objects.get_or_create(
                userId=userId,
                defaults={'lastSeenLocation': loc},
            )
            if not created:
                usr.lastSeenLocation.delete()
                usr.lastSeenLocation = loc
                usr.save() 
               # usr = User(userId = userId, lastSeenLocation = loc)
           # else:
           #     usr = User.objects.get(userId = session['id']) 
           #     usr.lastSeenLocation = loc
           # usr.save()

            print('User ID: {id}'.format(id = session['id']))
            

            #Returning same data back to browser
            data = {"lat":lat , "lon" : lon, 'time' : currentTime}
            return JsonResponse(data)
    
    #Get goes here
    # return known locations as json
    users = User.objects.all()
    locationsDict = dict(locations = [model_to_dict(user.lastSeenLocation) for user in users])
    return JsonResponse(locationsDict)

