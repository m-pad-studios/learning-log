import json

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse, Http404
from django.db.models import Sum
from .models import Topic, Entry, WorkoutCard
from .forms import TopicForm, EntryForm, WorkoutForm
from json import dumps
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
    topic = Topic.objects.get(id=topic_id)
    check_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

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
            return redirect('learning_logs:topic', workout_id=workout.id)
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
        raise Http404

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


def topic_chart(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    
    
    topics_sum = len(topics)
    user_topics = []
    user_entries = []

    # Topic data chart
    for topic in topics:
        
      user_topics.append(topic.text)
      user_entries.append(topics_sum)


    entry_sum = 0
    num_entries = []
    
    # Entries data chart
    for topic in topics:
        
        topic = Topic.objects.filter(owner=request.user).get(id=topic.id)
        entries = topic.entry_set.order_by('-date_added')
        for entry in entries:
            entry_sum += 1 + entry.id
            
    num_entries.append(entry_sum)
  
    chart_list = {
  
            "title": "Test",
            "label": "Time"
    }

    return chart_list

def entries_chart():
    topics = Topic.objects.order_by('date_added')
    
    entry_sum = 0
    num_entries = []
    
    # Entries data chart
    for topic in topics:
        
        topic = Topic.objects.get(id=topic.id)
        entries = topics.entry_set.order_by('-date_added')
        for entry in entries:
            entry_sum += 1
            
    num_entries.append(entry_sum)
    chart = {

                'topics':topics, 
               'num_entries':num_entries,
               'entry_sum':entry_sum,
               'choice_color':['rgba(110, 252, 250, 0.55)'] * entry_sum,
               'choice_border_color': ['rgba(0, 25, 250, 0.9)'] * entry_sum,
    }
    return chart
@login_required()
def charts(request):
    user_topics = topic_chart(request)


    
   
    workouts = WorkoutCard.objects.order_by('date_added')
    

    
    workout_sum = len(workouts)
    
    pr_sum = 0

    

    

    workout_names = []
    num_workouts = []

    # Workouts data chart
    for workout in workouts:
        workout_names.append(workout.name)
        num_workouts.append(workout_sum)

    pr_length = []
    pr_nums = []
    # PRs data from workouts chart
    for workout in workouts:
        
        if workout.pr_met == True:
            pr_length.append(workout.name)
            pr_sum += 1
            
    pr_nums.append(pr_sum)
    
    context = {
        'user_topics': user_topics,
      
    }
    
    return render(request, 'learning_logs/charts.html', user_topics)
