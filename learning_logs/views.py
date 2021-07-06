import json

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse
from django.db.models import Sum
from .models import Topic, Entry, WorkoutCard, WorkoutDeck
from .forms import TopicForm, EntryForm, WorkoutForm, WorkoutDeckForm
from polls.models import Choice, Question
from django.shortcuts import redirect
from json import dumps
from django.views.generic import TemplateView

# Pages section

""" 
Home pages
"""

def index(request):
    """The home page for Learning Log."""

    return render(request, 'learning_logs/index.html')


@login_required()
def home_dash(request):
    """The main dashboard for users"""
    return render(request, 'learning_logs/home_dash.html')

def check_owner(request, topic_id):

    topic = topic_id
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        return render(request, 'learning_logs/404.html')
"""
Topic pages
"""
@login_required()
def topic(request, topic_id):
    """Show a single topic and all its entries. """
    try:
        topic = Topic.objects.get(id=topic_id)
        check_owner(request, topic)

        entries = topic.entry_set.order_by('-date_added')
        context = {'topic': topic, 'entries': entries}
        return render(request, 'learning_logs/blogging/topic.html', context)
    except entries.DoesNotExist:
        return (request, 'learning_logs/404.html')

@login_required()
def delete_topic(request, topic_id):
    """Delete topic and all its entries. """
    topic = Topic.objects.get(id=topic_id)

    topic.delete()
    context = {}
    return render(request, 'learning_logs/blogging/delete_topic.html', context)

@login_required()
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/blogging/topics.html', context)


@login_required()
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

        if nw_copy == topic:
            print("CAN'T HAVE DUPLICATE TOPIC")
            return True

@login_required()
def new_topic(request):
    """Add a new topic."""

    if request.method != 'POST':
        # No data submitted; create a blank form.
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
    return render(request, 'learning_logs/blogging/new_topic.html', context)

"""
Entry pages
"""

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
    return render(request, 'learning_logs/blogging/new_entry.html', context)


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
    return render(request, 'learning_logs/blogging/edit_entry.html', context)

@login_required()
def delete_entry(request, entry_id):
    """Delete an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure the proper owner is the one editing.
    check_owner(request, topic)

    entry.delete()
    context = {'entry': entry, 'topic': topic}
    return render(request, 'learning_logs/blogging/delete_entry.html', context)


"""
Workout pages
"""

@login_required()
def start_workout(request):
    workouts = WorkoutCard.objects.filter(
        owner=request.user).order_by('date_added')
    workout_deck = WorkoutDeck.objects.order_by('date_added')
    context = {'workouts': workouts, 'workout_deck': workout_deck}
    return render(request, 'learning_logs/fitness/start_workout.html', context)

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
    context = {'workout': workout, 'form': form}
    return render(request, 'learning_logs/fitness/edit_workout.html', context)


@login_required()
def new_workout(request):
    """Add a new workout."""
    workouts = WorkoutCard.objects.filter(
        owner=request.user).order_by('date_added')
    if request.method != 'POST':
        # No data submitted; create a blank form.
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
    return render(request, 'learning_logs/fitness/new_workout.html', context)


@login_required()
def workout(request, workout_id):
    """Show a single workout card. """
    workout = WorkoutCard.objects.get(id=workout_id)
    
    context = {'workout': workout}
    return render(request, 'learning_logs/fitness/workout.html', context)


@login_required()
def workouts(request):
    """Show all workouts."""
    workouts = WorkoutCard.objects.filter(owner=request.user).order_by('date_added')
    workout_deck = WorkoutDeck.objects.order_by('date_added')

    print(workout_deck)

    context = {'workouts': workouts, 'workout_deck': workout_deck}
    return render(request, 'learning_logs/fitness/workouts.html', context)

@login_required()
def new_workout_deck(request):
    """ 
    Create a workout deck.
    """
  
        # POST data submitted; process data.
    form = WorkoutDeckForm(data=request.POST)

    if form.is_valid():

        new_deck = form.save(commit=False)
        new_deck.owner = request.user
        new_deck.text = new_deck.workouts_built_deck.details()
        new_deck.save()
            
        return redirect('learning_logs:workouts')

            # Check to make sure no duplicate topic is made
     
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/fitness/new_workout_deck.html', context)



@login_required()
def delete_workout(request, workout_id):
    """Delete a workout"""
    workout = WorkoutCard.objects.get(id=workout_id)

    workout.delete()
    context = {}
    return render(request, 'learning_logs/fitness/delete_workout.html', context)


"""
Charts

"""
@login_required()
def charts(request):

    def charts_view():
        q = Question.objects.get(pk=1)
      
        color_name = []
        context = {}
    

        color_name.append(q.choice_set.all())
        print(color_name)

        blue = str(color_name[0][0])
        red = str(color_name[0][1])
        orange = str(color_name[0][2])
        green = str(color_name[0][3])
        purple = str(color_name[0][4])
        yellow = str(color_name[0][5])
        black = str(color_name[0][6])
        white = str(color_name[0][7])
        pink = str(color_name[0][8])

        bv = color_name[0][0].votes
        rv = color_name[0][1].votes
        ov = color_name[0][2].votes
        gv = color_name[0][3].votes
        pv = color_name[0][4].votes
        yv = color_name[0][5].votes
        blv = color_name[0][6].votes
        wv = color_name[0][7].votes
        pv_v = color_name[0][8].votes

        votes = [bv,rv,ov,gv,pv,yv,blv, wv, pv_v]
        context["votes"] = votes
    
        if blue == "Blue":
            print("BLUE")
          
            context["blue"] = blue
            
        
        if red == "Red":
            print("RED")

            context["red"] = red
        
        if orange == "Orange":
            print("ORANGE")

            context["orange"] = orange

        if green == "Green":
            print("GREEN")

            context["green"] = green

        if purple == "Purple":
            print("PURPLE")

            context["purple"] = purple

        if yellow == "Yellow":
            print("YELLOW")

            context["yellow"] = yellow

        if black == "Black":
            print("BLACK")

            context["black"] = black

        if white == "White":
            print("WHITE")

            context["white"] = white 
        
        if pink == "Pink":
            print("PINK")

            context["pink"] = pink


     
        return context

    def workouts_charts():
        user_workouts = WorkoutCard.objects.all()
        name = []
        context = {}
        counter = []
        for wrk in user_workouts:
            name.append(wrk.name)
            #print(wrk.name)
            context = {"workouts": wrk.name}
            counter.append(wrk.id)
        return counter

    def topics_charts():
        user_topics = Topic.objects.all()
        name = []
        context = {}
        counter = []
        for tp in user_topics:
            name.append(tp.text)
            #print(tp.text)
            context = {"topics": tp.text}
            counter.append(tp.id)
        return counter

    def my_own_charts():

        my_topics = Topic.objects.filter(owner=request.user).order_by('date_added')
        my_workouts = WorkoutCard.objects.filter(owner=request.user).order_by('date_added')

    
        my_topic_name = []
        context = {}
        counter = []
        counter_2 = []
        total_counters = []

        for tp in my_topics:
            my_topic_name.append(tp.text)
            #print(tp.text)
            context = {"my_topics": tp.text}
            counter.append(tp.id)


        my_workout_name = []
        context_2 = {}

        for w in my_workouts:
            my_workout_name.append(w.name)
            #print(w.name)
            context_2 = {"my_workouts": w.name}
            counter_2.append(w.id)

        total_counters.append(counter)
        total_counters.append(counter_2)
        return total_counters

        
    logged_user = request.user.id    
    
    
    ctx = {"workouts": workouts_charts(), "topics": topics_charts(), "polls_color": charts_view(), "my_stats": my_own_charts(), "logged_user": logged_user}
    print(ctx)

    return render(request, 'learning_logs/charts.html', {'serialized_data': json.dumps(ctx)})


""" 
Custom errors

"""
def error_404_view(request, exception):
    data = {}
    return render(request, 'learning_logs/404.html', data)
