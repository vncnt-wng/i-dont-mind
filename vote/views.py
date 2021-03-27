from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Choice, Room


def home(request):
    if request.method == "POST":
        room_id = request.POST.get("room_id", "")
        if room_id != "": # and other logic
            return redirect("{}/vote".format(room_id))
    return render(request, "home.html", {})

def create(request):
    #return render(request, "home.html", {})
    return HttpResponse("Create.")

def vote(request, room_id):
    question = get_object_or_404(Room, room_id=room_id).question
    choices = get_object_or_404(Choice, question=question)
    return render(request, 'polls/detail.html', {'choice': choices})
    #return HttpResponse("You're looking at voting room %s." % room_id)

def results(request, room_id):
    return HttpResponse("You're looking at results room %s." % room_id)