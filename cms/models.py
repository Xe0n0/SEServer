from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.forms import ModelForm

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    time = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    organizer = models.CharField(max_length=200)
    content = models.TextField()
    follower = models.ManyToManyField(User, blank=True)
    tags = TaggableManager(blank=True)

class Game(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    tags = TaggableManager()

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    realname = models.CharField(max_length=75, default='')
    nickname = models.CharField(max_length=75, default='')
    gender = models.IntegerField(default=0)
    tags = TaggableManager()
    age = models.IntegerField(default=0)

class ActivityForm(ModelForm):

    class Meta:
        model = Activity
        exclude = ('tags', 'organizer')