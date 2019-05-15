from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def index(request):
    return render(request, 'calorie/index.html', {'nbar': 'home'})

def calories(request):
    return render(request, 'calorie/calories.html', {'nbar': 'calories'})

def sleep(request):
    return render(request, 'calorie/sleep.html', {'nbar': 'sleep'})

def mood(request):
    return render(request, 'calorie/mood.html', {'nbar': 'mood'})
