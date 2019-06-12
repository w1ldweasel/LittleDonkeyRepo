from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Match, Team


def football(request):
#    return HttpResponse("Hello visitor. team:-")
    
    teams = Team.objects.all()
    return render(request, 'football/index.html', {'teams': teams})




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
        
