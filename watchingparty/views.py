"""
REFERENCES

Title: <Openrouteservice Directions Service (GET)>
Author: <Openrouteservice>
URL: <https://openrouteservice.org/dev/#/api-docs/v2/directions/{profile}/get>

Title: <How to create a meeting with zoom API in Python?>
Date: <January 19th, 2022>
Code version: <Python 3>
URL: <https://www.geeksforgeeks.org/how-to-create-a-meeting-with-zoom-api-in-python/>

"""

from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .forms import ProfileForms
import requests
import json
import geocoder
import jwt
from time import time
from .models import Event, Profile, Meeting
from django.views.generic import TemplateView, ListView
from django.db.models import Q

def index(request):
    card_set = Event.objects.all()
    temp = loader.get_template('index.html')
    context = {
        'events': card_set,
    }
    if request.user.is_authenticated:
        if(Profile.objects.filter(userName=request.user).last() == None):
            currentUser = Profile(interests="", userName=request.user, firstFavoriteMovie="",
                            secondFavoriteMovie="", thirdFavoriteMovie="", fourthFavoriteMovie="",
                            fifthFavoriteMovie="", firstFavoriteTVShow="", secondFavoriteTVShow="", 
                            thirdFavoriteTVShow="", fourthFavoriteTVShow="", fifthFavoriteTVShow="")
            currentUser.save()
    return render(request, 'index.html', context)


def deleteEvent(request, movietitle, description):
    profile = Profile.objects.filter(userName=request.user).last()
    events = Event.objects.filter(participant=profile)
    event = Event.objects.filter(mediaTitle__exact=movietitle, description__exact=description).last()
    event.participant.remove(profile)
    print(movietitle)
    print(description)
    return render(request, 'profileDetail.html', {'profile': profile, 'events': events})


def profileDetail(request):
    profile = Profile.objects.filter(userName=request.user).last()
    if request.method == 'POST':
        messages.success(request, "You have been added to a new event!")
        # need to use .filter for M-to-M relationships
        event = Event.objects.filter(mediaTitle__exact=request.POST["eventName"]).last()
        event.participant.add(profile)
    events = Event.objects.filter(participant=profile)
    print(events.values())
    return render(request, 'profileDetail.html', {'profile': profile, 'events': events})


def generateToken():
    token = jwt.encode({'iss': 'dWC4PepmTZOX2yJldbmbjA', 'exp': time() + 5000}, 'IOe2IfGpjP5WkDCeLaXXH6Fgem8Zz8pnUh8m',
                       algorithm='HS256')
    return token


def createMeeting(startTime, city, username, movieTitle):
    meetingdetails = {"topic": "WatchParty to watch " + movieTitle + " with " + username,
                      "type": 2,
                      "start_time": startTime,
                      "duration": "180",
                      "timezone": "US/" + city,
                      "agenda": "Watching movies / TV shows",

                      "settings": {"host_video": "true",
                                   "participant_video": "true",
                                   "join_before_host": "False",
                                   "mute_upon_entry": "False",
                                   "watermark": "false",
                                   "audio": "voip",
                                   "auto_recording": "none",
                                   "enforce_login": "true",
                                   }
                      }
    headers = {'authorization': 'Bearer ' + generateToken(),
               'content-type': 'application/json'}
    zoomData = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))
    jsonZoomData = json.loads(zoomData.text)
    return jsonZoomData


def settingsDetail(request):
    return render(request, 'profileSettingsDetail.html', {})


def profileSettings(request):
    if request.method == 'POST':
        interests = request.POST["interests"]
        firstFavoriteMovie = request.POST["firstFavoriteMovie"]
        secondFavoriteMovie = request.POST["secondFavoriteMovie"]
        thirdFavoriteMovie = request.POST["thirdFavoriteMovie"]
        fourthFavoriteMovie = request.POST["fourthFavoriteMovie"]
        fifthFavoriteMovie = request.POST["fifthFavoriteMovie"]
        firstFavoriteTVShow = request.POST["firstFavoriteTVShow"]
        secondFavoriteTVShow = request.POST["secondFavoriteTVShow"]
        thirdFavoriteTVShow = request.POST["thirdFavoriteTVShow"]
        fourthFavoriteTVShow = request.POST["fourthFavoriteTVShow"]
        fifthFavoriteTVShow = request.POST["fifthFavoriteTVShow"]
        profile = Profile.objects.filter(userName = request.user)
        profile.update(interests=interests, firstFavoriteMovie=firstFavoriteMovie,
                          secondFavoriteMovie=secondFavoriteMovie,
                          thirdFavoriteMovie=thirdFavoriteMovie, fourthFavoriteMovie=fourthFavoriteMovie,
                          fifthFavoriteMovie=fifthFavoriteMovie, firstFavoriteTVShow=firstFavoriteTVShow,
                          secondFavoriteTVShow=secondFavoriteTVShow, thirdFavoriteTVShow=thirdFavoriteTVShow,
                          fourthFavoriteTVShow=fourthFavoriteTVShow, fifthFavoriteTVShow=fifthFavoriteTVShow)
        return HttpResponseRedirect(reverse('watchingparty:profile'))

    return render(request, 'profileSettingsDetail.html', {})


def planMovie(request):
    if request.method == 'POST':
        title = request.POST["mediaTitle"]
        user = request.user.username
        print(request.scheme)
        time = request.POST["eventDate"]
        describe = request.POST["description"]
        temp = request.POST["platform"]
        address = request.POST["address"]
        city = ""
        curProf = Profile.objects.get(userName__exact=request.user)
        x = Event(mediaTitle=title, username=user,
                  eventDate=time, description=describe,
                  platform=temp, address=address,
                  city=city, creator=curProf)
        x.save()
        print("Am I inside this post request")
        if temp != "movieStock.jpeg":
            zoomData = createMeeting(time, city, user, title)
            join_URL = zoomData["join_url"]
            meetingPassword = zoomData["password"]
            meeting = Meeting(link=join_URL, password=meetingPassword, username=user, movieTitle=title)
            meeting.save()
        return render(request, 'PlanMovie.html', {})
        # return HttpResponse(temp.render(request))
        # return HttpResponseRedirect('index') # goto main page so user sees new addition

    return render(request, 'PlanMovie.html', {})

def movieInfo(request, movietitle, description):
    movie = Event.objects.filter(mediaTitle=movietitle).filter(description=description).last()
    if movie.platform == "movieStock.jpeg":
        locationData = requests.get(
            f"https://api.openrouteservice.org/geocode/search?api_key=5b3ce3597851110001cf62487a5f0088845f4bf7baed2d3f23d802e9&text={movie.address}")
        jsonLocationData = json.loads(locationData.text)
        featuresData = jsonLocationData["features"]
        data = featuresData[0]
        geometryData = data["geometry"]
        coordinates = geometryData["coordinates"]
        finishLongitude = coordinates[0]
        finishLongitudeString = str(finishLongitude)
        finishLatitude = coordinates[1]
        finishLatitudeString = str(finishLatitude)
        # Include this in production
        # ip = request.META.get('REMOTE_ADDR', None)
        g = geocoder.ip('me')
        startLongitude = g.lng
        startLongitudeString = str(startLongitude)
        startLatitude = g.lat
        startLatitudeString = str(startLatitude)
        directionData = requests.get(
            f'https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf62487a5f0088845f4bf7baed2d3f23d802e9&start={startLongitudeString},{startLatitudeString}&end={finishLongitudeString},{finishLatitudeString}')
        jsonDirectionData = json.loads(directionData.text)
        jsonDirectionData2 = jsonDirectionData["features"]
        jsonDirectionData3 = jsonDirectionData2[0]
        jsonDirectionData4 = jsonDirectionData3["properties"]
        jsonDirectionData5 = jsonDirectionData4["segments"]
        jsonDirectionData6 = jsonDirectionData5[0]
        jsonDirectionData7 = jsonDirectionData6["steps"]
        instructions = []
        for step in jsonDirectionData7:
            instructions.append(step["instruction"])
        return render(request, 'MovieInfo.html',
                      {'event': movie, 'coordinates': coordinates, 'instructions': instructions, })

    else:
        meeting = Meeting.objects.filter(username=movie.username, movieTitle=movie.mediaTitle).last()
        zoomLink = meeting.link
        zoomPassword = meeting.password
        return render(request, 'MovieInfo.html',
                      {'event': movie, 'link': zoomLink, 'password': zoomPassword, })
class SearchView(TemplateView):
        template_name = 'search.html'

class SearchResultsView(ListView):
    model = Event
    template_name = 'searchResults.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Event.objects.filter(
            Q(mediaTitle__icontains=query) | Q(username__contains=query)
        )
        return object_list