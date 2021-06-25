"""Defines URL patterns for learning_logs. """

from django.urls import path
from django.conf.urls import handler404, handler500, handler403, handler400
from learning_logs import views

app_name = 'learning_logs'

handler404 = 'learning_logs.views.error_404_view'

urlpatterns = [
    #Home page 
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page to view charts.
    path('charts/', views.charts, name='charts'),
    # Page for creating workout cards
    path('new_workout/', views.new_workout, name='new_workout'),
    # Page to all your workout cards created 
    path('workouts/', views.workouts, name='workouts'),
    # Detail page for a single workout
    path('workout/<int:workout_id>/', views.workout, name='workout'),
    # Page that notifies entry has been deleted
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    # Page that notifies topic has been deleted
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    # Page that notifies workout has been deleted
      path('delete_workout/<int:workout_id>/', views.delete_workout, name='delete_workout'),
      # Page for home dashboard when you login
      path('home_dash/', views.home_dash, name='home_dash'),
      # Page for editing workouts
      path('edit_workout/<int:workout_id>/', views.edit_workout, name='edit_workout'),
      # Page for 404
    
   
]