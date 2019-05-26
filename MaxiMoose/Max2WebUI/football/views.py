from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

def football(request):
    return HttpResponse("Hello visitor . You're at the football home page.")
