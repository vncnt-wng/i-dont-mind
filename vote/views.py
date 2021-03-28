import random
import string
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Room, Question, Choice

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
    room_id = ''.join(random.choice(string.ascii_uppercase) for i in range(0, 6))
    query = Room.objects.filter(room_id=room_id)
    while query.count() >= 1:
        room_id = ''.join(random.choice(string.ascii_lowercase) for i in range(0, 6))
        query = Room.objects.filter(room_id=room_id)
    question = Question(question_text="dummy", pub_date=timezone.now())
    question.save()
    room = Room(question=question, room_id=room_id, room_name="dummy")
    room.save()
    print(room_id)
    return HttpResponse("Create.")

def vote(request, room_id):
    question = get_object_or_404(Room, room_id=room_id).question
    choices = Choice.objects.filter(question=question)

    return render(request, 'vote.html', data={
        'question': question,
        'choices' : choices
    })
    #return HttpResponse("You're looking at voting room %s." % room_id)


#def make_colours()

def results(request, room_id):
    question = get_object_or_404(Room, room_id=room_id).question
    choices = Choice.objects.filter(question=question)
    labels = []
    votes = []
    greatestChoice = choices[0]

    for choice in choices:
        labels.append(choice.choice_text)
        votes.append(choice.votes)
        if choice.votes > greatestChoice.votes:
            greatestChoice = choice

    return render(request, 'results.html', {
        'labels' : labels,
        'votes' : votes,
        'winner' : greatestChoice
    })