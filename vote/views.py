from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html", {})

def create(request):
    return render(request, "home.html", {})

def vote(request, room_id):
    return HttpResponse("You're looking at voting room %s." % room_id)

def results(request, room_id):
    return HttpResponse("You're looking at results room %s." % room_id)