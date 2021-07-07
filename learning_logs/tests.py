import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Topic
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your tests here.

"""
Method factory.
"""


def create_topic(text, days, owner):

    time = timezone.now() + datetime.timedelta(days=days)
    return Topic.objects.create(text=text, date_added=time, owner=owner)


"""
Unit tests for Question model
"""


class TopicModelTests(TestCase):

    def test_was_published_recently(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_topic = Topic(date_added=time)
        self.assertIs(future_topic.was_published_recently(), False)

    def test_was_published_recently_with_old_topic(self):

        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_topic = Topic(date_added=time)
        self.assertIs(old_topic.was_published_recently(), False)

    def test_was_published_recently_with_recent_topic(self):

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_topic = Topic(date_added=time)
        self.assertIs(recent_topic.was_published_recently(), True)


class TopicIndexViewTests(TestCase):

    def test_no_topics(self):

        response = self.client.get(reverse('learning_logs:topics'))
        self.assertEqual(response.status_code, 302)

    def test_past_topic(self):

        topic = create_topic(text="Past topic.", days=-30)

    def test_future_topic(self):

        create_topic(text="Future topic.", days=30)
        response = self.client.get(reverse('learning_logs:index'))
        self.assertContains(response, "No topics are available.")

        self.assertQuerysetEqual(response.context['latest_topic_list'], [])

    def test_future_topic_and_past_topic(self):

        user = User.objects.create(id=0,  username='M')
        topic = create_topic(text="Past topic.",  days=-30, owner=user)
        response = self.client.get(reverse('learning_logs:topics'))
        self.assertQuerysetEqual(
            response.context['latest_topic_list'], [topic])

    def test_two_past_topics(self):

        user = User.objects.create(id=0,  username='M')
        user2 = User.objects.create(id=1, username='P')
        topic1 = create_topic(text="Past topic 1.", days=-30, owner=user)
        topic2 = create_topic(text="Past topic 2.", days=-5, owner=user2)
        response = self.client.get(reverse('learning_logs:topics'))


class TopicDetailViewTests(TestCase):

    def test_future_topic(self):
        future_topic = create_topic(text='Future topic', days=5)
        url = reverse('learning_logs:index', args=(future_topic.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_topic(self):
        user = User.objects.create(id=0,  username='M')
        past_topic = create_topic(text='Past topic.', days=-5, owner=user)
        response = self.client.get('learning_logs:topics')

        self.assertEqual(response.status_code, 404)
