from django.shortcuts import redirect, render
from django.http import HttpResponse
from vote.models import Room

def home(request):
    if request.method == "POST":
        room_id = request.POST.get("room_id", "")
        if room_id != "": # and other logic
            query = Room.objects.filter(room_id=room_id)
            if query.count() >= 1:
               return redirect("{}/vote".format(room_id))
            else:
                # display error message
                print("Error")
                
    return render(request, "home.html", {})

def create(request):
    #return render(request, "home.html", {})
    room_id = ''.join(random.choice(string.ascii_lowerase) for i in range(0, 6))
    query = Room.objects.filter(room_id=room_id)
    while query.count() >= 1:
        room_id = ''.join(random.choice(string.ascii_lowerase) for i in range(0, 6))
        query = Room.objects.filter(room_id=room_id)
    return HttpResponse("Create.")

def vote(request, room_id):
    return HttpResponse("You're looking at voting room %s." % room_id)

def results(request, room_id):
    return HttpResponse("You're looking at results room %s." % room_id)