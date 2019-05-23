from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView

from calorie.forms import *
from calorie.models import *

import datetime

# Create your views here.
def index(request):
    return render(request, 'calorie/index.html', {'nbar': 'home'})

@login_required
def calories(request):
    upi = UserProfileInfo.objects.get(user=request.user)
    today = datetime.datetime.today()
    entry_exists = Entry.objects.filter(date_for=today).exists()
    obj_exists = False

    if entry_exists:
        entry = Entry.objects.get(date_for=today)
        obj_exists = Calorie.objects.filter(entry=entry).exists()
        if obj_exists:
            obj = Calorie.objects.get(entry=Entry.objects.get(date_for=today))

    if request.method == 'POST':
        if obj_exists:
            calorie_form = CalorieForm(data=request.POST, instance=obj)
        else:
            calorie_form = CalorieForm(data=request.POST)

        if calorie_form.is_valid():
            calorie = calorie_form.save(commit=False)
            if entry_exists:
                entry = Entry.objects.get(date_for=today)
                entry.date_modified = today
                entry.save()
            else:
                entry = Entry(user=upi)
                entry.save()
            calorie.entry = entry
            calorie.save()
    else:
        if obj_exists:
            calorie_form = CalorieForm(instance=obj)
        else:
            calorie_form = CalorieForm()

    context = {
        'nbar': 'calories',
        'calorie_form': calorie_form,
        'today': str(datetime.date.today().strftime("%m/%d/%Y")),
        # 'entry_exists': entry_exists,
    }
    return render(request, 'calorie/calories.html', context)

@login_required
def sleep(request):
    # upi = UserProfileInfo.objects.get(user=request.user)
    # sleep_exists = Sleep.objects.filter(user=upi).exists()
    today = datetime.datetime.today()
    # entry_exists = Entry.objects.filter(date_for=today).exists()

    if request.method == 'POST':
        sleep_form = SleepForm(data=request.POST)
        # if entry_exists:
        #     sleep_form = SleepForm(data=request.POST, instance=obj)
        # else:
        #     sleep_form = SleepForm(data=request.POST)

    else:
        sleep_form = SleepForm()
        # if entry_exists:
        #     sleep_form = SleepForm(instance=obj)
        # else:
        #     sleep_form = SleepForm()

    context = {
        'nbar': 'sleep',
        'sleep_form': sleep_form,
        'today': str(datetime.date.today().strftime("%m/%d/%Y")),
        # 'entry_exists': entry_exists,
    }
    return render(request, 'calorie/sleep.html', context)

@login_required
def mood(request):
    upi = UserProfileInfo.objects.get(user=request.user)
    today = datetime.datetime.today()
    entry_exists = Entry.objects.filter(date_for=today).exists()
    obj_exists = False

    if entry_exists:
        entry = Entry.objects.get(date_for=today)
        obj_exists = Mood.objects.filter(entry=entry).exists()
        if obj_exists:
            obj = Mood.objects.get(entry=Entry.objects.get(date_for=today))

    if request.method == 'POST':
        if obj_exists:
            mood_form = MoodForm(data=request.POST, instance=obj)
        else:
            mood_form = MoodForm(data=request.POST)

        if mood_form.is_valid():
            mood = mood_form.save(commit=False)
            if entry_exists:
                entry = Entry.objects.get(date_for=today)
                entry.date_modified = today
                entry.save()
            else:
                entry = Entry(user=upi)
                entry.save()
            mood.entry = entry
            mood.save()
            print(mood.mood_time)
    else:
        if obj_exists:
            mood_form = MoodForm(instance=obj)
        else:
            mood_form = MoodForm()

    context = {
        'nbar': 'mood',
        'mood_form': mood_form,
        'today': str(datetime.date.today().strftime("%m/%d/%Y")),
        # 'entry_exists': entry_exists,
    }
    return render(request, 'calorie/mood.html', context)

@login_required
def profile(request):
    upi = UserProfileInfo.objects.get(user=request.user)
    setup_exists = Setup.objects.filter(user=upi).exists()
    name = ''
    if setup_exists:
        obj = Setup.objects.get(user=upi)
        name = obj.first_name + ' ' + obj.last_name

    if request.method == 'POST':
        if setup_exists:
            setup_form = SetupForm(data=request.POST, instance=obj)
        else:
            setup_form = SetupForm(data=request.POST)

        if setup_form.is_valid():
            setup = setup_form.save(commit=False)
            setup.user = upi
            setup.save()
    else:
        if setup_exists:
            setup_form = SetupForm(instance=obj)
        else:
            setup_form = SetupForm()

    context = {
        'nbar': 'profile',
        'setup_form': setup_form,
        'setup_exists': setup_exists,
        'name': name,
    }
    return render(request, 'calorie/profile.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'calorie/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'calorie/login.html', {})
