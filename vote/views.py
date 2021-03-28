import random
import string
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Room, Question, Choice
from .forms import QuestionForm, ChoiceForm
from django.forms.models import inlineformset_factory

def home(request):
    if request.method == "POST":
        room_id = request.POST.get("room_id", "")
        if room_id != "": # and other logic
            query = Room.objects.filter(room_id=room_id)
            if query.count() >= 1:
               return redirect("vote", room_id)
            else:
                # display error message
                print("Error")
                
    return render(request, "home.html", {})


def get_room_id(request):
    room_id = ''.join(random.choice(string.ascii_uppercase) for i in range(0, 6))
    query = Room.objects.filter(room_id=room_id)
    while query.count() >= 1:
        room_id = ''.join(random.choice(string.ascii_lowercase) for i in range(0, 6))
        query = Room.objects.filter(room_id=room_id)
    return redirect("create_question", room_id)


def create_question(request, room_id):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data["question_text"]
            question = Question(question_text=question_text, pub_date=timezone.now())
            question.save()
            room = Room(question=question, room_id=room_id, room_name="")
            room.save()
            return redirect("create_choices", room_id)
    form = QuestionForm()
    return render(request, "create_question.html", {'form':form})


def create_choices(request, room_id):

    room = Room.objects.filter(room_id=room_id)[0]

    choice_formset = inlineformset_factory(Question, Choice, form=ChoiceForm,
        fields=['choice_text'], extra=1, can_delete=True
    )  

    if request.method == "POST":
        formset = choice_formset(request.POST, instance=room.question)
        if formset.is_valid():
            formset.save()
            return redirect('create_choices', room_id)

    formset = choice_formset(instance=room.question)
    return render(request, 'create_choices.html', {
        'formset': formset,
        'room_id': room_id
    })


def vote(request, room_id):
    question = get_object_or_404(Room, room_id=room_id).question
    choices = Choice.objects.filter(question=question)

    if request.method == "POST":
        room_id = request.POST.get("room_id", "")
        choice = request.POST.get("choice", "")
        chosen = choices.filter(choice_text=choice)[0]
        chosen.votes += 1
        chosen.save()
        return redirect("results", room_id)

    return render(request, 'vote.html', {
        'question': question,
        'choices' : choices,
        'room_id' : room_id
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
    return HttpResponse("You're looking at results room %s." % room_id)

def about(request):
    return render(request, "about.html", {})
