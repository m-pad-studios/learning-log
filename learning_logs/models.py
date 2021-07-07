import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about. """

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_added <= now

    def __str__(self):
        """Return a string representation of the model. """
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."

class WorkoutCard(models.Model):
    """A customizable workout card"""

    name = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()
    pr_met = models.BooleanField(default=False)
    sets_completed = models.IntegerField()
    reps_completed = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.name[:50]}..."

    def details(self):

        return f"{self.name, self.sets, self.reps, self.owner}"


class WorkoutDeck(models.Model):
    """A customizable workout deck to place Workout cards """

    workouts_built_deck = models.ForeignKey(WorkoutCard, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
