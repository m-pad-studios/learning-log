from django import forms

from .models import Topic, Entry, WorkoutCard, WorkoutDeck

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutCard
        fields = ['name','sets','reps','pr_met','sets_completed','reps_completed']
        labels = {'name': 'Name', 'sets': 'Sets','reps': 'Reps','pr_met': '<-- Check if you made your PR Today in this workout','sets_completed': 'Sets you were able to complete','reps_completed': 'Reps you were able to complete',}

class WorkoutDeckForm(forms.ModelForm):
    class Meta:
        model = WorkoutDeck
        workouts = WorkoutCard.objects.all()
        workouts_details = [""]
        fields = ['name', 'workouts_built_deck', 'text']
        labels = {'text': workouts_details}
        widgets = {'text': forms.HiddenInput()}

       