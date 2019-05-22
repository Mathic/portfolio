from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

import datetime
import plotly.plotly as py
import plotly.graph_objs as go

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Setup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=3, decimal_places=3, default=0)
    age = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    gender = models.CharField(max_length=25)
    weight = models.DecimalField(max_digits=3, decimal_places=3, default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Entry(models.Model):
    date_for = models.DateField(default=datetime.date.today)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    setup = models.ForeignKey(Setup, on_delete=models.CASCADE)

class Calorie(models.Model):
    entry_weight = models.DecimalField(max_digits=3, decimal_places=3, default=0)
    calories_in = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    calories_out = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

class Sleep(models.Model):
    time_awake = models.DateTimeField(blank=True)
    time_slept = models.DateTimeField(blank=True)
    sleep_duration = models.DurationField()

class Exercise(models.Model):
    exercise_duration = models.DurationField()
    heart_rate = models.IntegerField(default=0)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
