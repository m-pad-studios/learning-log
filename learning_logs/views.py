import json
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse
from django.db.models import Sum
from .models import Topic, Entry, WorkoutCard
from .forms import TopicForm, EntryForm, WorkoutForm
from django.shortcuts import redirect
from json import dumps
from django.views.generic import TemplateView

#Pages section

def index(request):
    """The home page for Learning Log."""
    
    return render(request, 'learning_logs/index.html')

@login_required()
def home_dash(request):
    """The main dashboard for users"""
    return render(request, 'learning_logs/home_dash.html')

@login_required()
def topic(request, topic_id):
    
    """Show a single topic and all its entries. """
    try:
        topic = Topic.objects.get(id=topic_id)
        check_owner(request, topic)
        
        entries = topic.entry_set.order_by('-date_added')
        context = {'topic': topic, 'entries': entries}
        return render(request, 'learning_logs/topic.html', context)
    except entries.DoesNotExist:
        return (request, 'learning_logs/404.html')


@login_required()
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required()
def new_topic(request):
    """Add a new topic."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        
        
        if form.is_valid():

            new_topic = form.save(commit=False)

            # Check to make sure no duplicate topic is made
            if check_topics(request, new_topic) == True:
                return redirect('/new_topic/')
            new_topic.owner = request.user
            new_topic.save()
    
            return redirect('learning_logs:topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required()
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    check_owner(request, topic)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required()
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure the proper owner is the one editing.
    check_owner(request, topic)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.

        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required()
def edit_workout(request, workout_id):
    """Edit an existing entry."""
    workout = WorkoutCard.objects.get(id=workout_id)
    
    # Make sure the proper owner is the one editing.
    check_owner(request, workout)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.

        form = WorkoutForm(instance=workout)
    else:
        # POST data submitted; process data.
        form = WorkoutForm(instance=workout, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:workout', workout_id=workout.id)
    context = { 'workout': workout, 'form': form}
    return render(request, 'learning_logs/edit_workout.html', context)

@login_required()
def new_workout(request):
    """Add a new topic."""
    workouts = WorkoutCard.objects.filter(owner=request.user).order_by('date_added')
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = WorkoutForm()
    else:
        # POST data submitted; process data.
        form = WorkoutForm(data=request.POST)
        
        
        if form.is_valid():

            new_topic = form.save(commit=False)

            # Check to make sure no duplicate topic is made
            if check_topics(request, new_topic) == True:
                return redirect('/new_topic/')
            new_topic.owner = request.user
            new_topic.save()
    
            return redirect('learning_logs:workouts')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_workout.html', context)
    
@login_required()
def workout(request, workout_id):
    """Show a single workout card. """
    workout = WorkoutCard.objects.get(id=workout_id)

    context = {'workout': workout}
    return render(request, 'learning_logs/workout.html', context)


@login_required()
def workouts(request):
    """Show all workouts."""
    workouts = WorkoutCard.objects.filter(owner=request.user).order_by('date_added')
    context = {'workouts': workouts}
    return render(request, 'learning_logs/workouts.html', context)

@login_required()
def delete_entry(request, entry_id):
    """Delete an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure the proper owner is the one editing.
    check_owner(request, topic)

    entry.delete()
    context = {'entry': entry, 'topic': topic}
    return render(request, 'learning_logs/delete_entry.html', context)

@login_required()
def delete_topic(request, topic_id):
    """Delete topic and all its entries. """
    topic = Topic.objects.get(id=topic_id)

    topic.delete()
    context = {}
    return render(request, 'learning_logs/delete_topic.html', context)

@login_required()
def delete_workout(request, workout_id):
    """Delete a workout"""
    workout = WorkoutCard.objects.get(id=workout_id)

    workout.delete()
    context = {}
    return render(request, 'learning_logs/delete_workout.html', context)
  
# Custom functions
def check_owner(request, topic_id):

    topic = topic_id
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        return render(request, 'learning_logs/404.html')

def check_topics(request, duplicate):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    copy = ""
    copy = str(duplicate)
    nw_copy = copy.strip().lower()
    copy_topics = []

    print("~~~~~~~~~~~~")
    print(nw_copy)
    print("~~~~~~~~~~~~~~~~~")
    for topic in topics:
        tp_copy = str(topic.text)
        nw_tp_copy = tp_copy.lower()
        copy_topics.append(nw_tp_copy)

    for topic in copy_topics:

        if nw_copy  == topic:
            print("CAN'T HAVE DUPLICATE TOPIC")
            return True


"""
Charts start here

 """




@login_required()
def charts(request):
    def charts_view():
 
        workout = WorkoutCard.objects.all()
        name = []
        context = {}
        counter = 0
        for w in workout:
            name.append(w.name)
            print(w.name)
            context = {"workouts": w.name}
            counter += 1
        return counter
    ctx = {"workout": charts_view()}
    
    print(ctx)
    return render(request, 'learning_logs/charts.html', {'serialized_data': json.dumps(ctx)})
    

      





def error_404_view(request, exception):
    data = {}
    return render(request, 'learning_logs/404.html', data)
    
