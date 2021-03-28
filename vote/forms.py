from django import forms
from .models import Choice, Question
from django.forms.models import inlineformset_factory

class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200)


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('choice_text',)

CollectionChoiceFormSet = inlineformset_factory(
    Question, Choice, form=ChoiceForm,
    fields=['choice_text'], extra=1, can_delete=True
)