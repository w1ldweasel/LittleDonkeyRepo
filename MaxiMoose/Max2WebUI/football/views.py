from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Match, Team
import urllib.request 
import json

def football(request):
#    return HttpResponse("Hello visitor. team:-")
    
#    teams = Team.objects.all()
#   return render(request, 'football/index.html', {'teams': teams})


  urlData = "https://apiv2.apifootball.com/?action=get_teams&league_id=149&APIkey=124&APIkey=


  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))
  if (webUrl.getcode() == 200):
      data = webUrl.read()

      theJSON = json.loads(data)
      print_json = json.dumps(theJSON, indent=4, sort_keys=True)
      print(json.dumps(theJSON, indent=4, sort_keys=True))
      return render(request, 'football/index.html', {'teams': print_json})
  # No results returned
  return render(request, 'football/error.html', {'error_message': 'no results'})

def results(request, number):

    teams = Team.objects.all()
    return render(request, 'football/index.html', {'teams': teams})


def match(request):
    return HttpResponse("Hello visitor . match results:")

    try:
        match = Match.objects.get(id=id)
        
    except Match.DoesNotExist:
        raise Http404('Page not found')
        
        
def nuts(request):
    return HttpResponse("Hello, world. You're at the football nuts page.")
        
