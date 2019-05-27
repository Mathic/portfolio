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
def profile(request):
    upi = UserProfileInfo.objects.get(user=request.user)
    setup_exists = Setup.objects.filter(user=upi).exists()

    if setup_exists:
        obj = Setup.objects.get(user=upi)
        name = obj.first_name + ' ' + obj.last_name
    else:
        name = request.user.username

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
        'name': name,
    }
    return render(request, 'calorie/profile.html', context)

# authentication
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

# calories
@login_required
def calories(request):
    context = {
        'nbar': 'calories',
        'today': str(datetime.datetime.today().strftime("%m/%d/%Y")),
    }
    return render(request, 'calorie/calories.html', context)

@login_required
def load_calorie(request):
    entry_obj = create_entry(request)
    calorie_form = populate_calorie_form(request, entry_obj)

    if request.method == 'POST':
        entry_form = EntryForm(data=request.POST, instance=entry_obj)

        if calorie_form.is_valid() and entry_form.is_valid():
            entry = entry_form.save(commit=False)
            entry.save()
            calorie = calorie_form.save(commit=False)
            calorie.entry = entry_obj
            calorie.save()
        else:
            print(calorie_form.errors,entry_form.errors)

        context = {
            'nbar': 'calories',
            'today': str(datetime.datetime.today().strftime("%m/%d/%Y")),
        }

        return render(request, 'calorie/calories.html', context)
    else:
        entry_form = EntryForm(instance=entry_obj)
        context = {
            'nbar': 'calories',
            'calorie_form': calorie_form,
            'entry_form': entry_form,
            'entry': entry_obj,
            'today': str(datetime.date.today().strftime("%m/%d/%Y")),
        }

        return render(request, 'calorie/calorie_info.html', context)

def load_calorie_table(request):
    upi = UserProfileInfo.objects.get(user=request.user)
    entries = Entry.objects.filter(user=upi).order_by('date_for')
    cals = Calorie.objects.filter(entry__in=entries)

    return render(request, 'calorie/calorie_table.html', {'cals': cals,})

# sleep
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
def load_sleep(request):
    return render(request, 'calorie/sleep.html')

# mood
@login_required
def mood(request):
    context = {
        'nbar': 'mood',
        'today': str(datetime.date.today().strftime("%m/%d/%Y")),
    }
    return render(request, 'calorie/mood.html', context)

@login_required
def load_mood(request):
    entry_obj = create_entry(request)
    mood_form = populate_mood_form(request, entry_obj)

    if request.method == 'POST':
        entry_form = EntryForm(data=request.POST, instance=entry_obj)

        if mood_form.is_valid() and entry_form.is_valid():
            entry = entry_form.save(commit=False)
            entry.save()
            mood = mood_form.save(commit=False)
            mood.entry = entry_obj
            mood.save()
        else:
            print(mood_form.errors,entry_form.errors)

        context = {
            'nbar': 'mood',
            'mood_form': mood_form,
        }
        return render(request, 'calorie/mood.html', context)
    else:
        entry_form = EntryForm(instance=entry_obj)
        context = {
            'nbar': 'mood',
            'mood_form': mood_form,
            'entry_form': entry_form,
            'entry': entry_obj,
            'today': str(datetime.date.today().strftime("%m/%d/%Y")),
        }
        return render(request, 'calorie/mood_info.html', context)

def load_mood_table(request):
    upi = UserProfileInfo.objects.get(user=request.user)
    entries = Entry.objects.filter(user=upi).order_by('date_for')
    moods = Mood.objects.filter(entry__in=entries)

    return render(request, 'calorie/mood_table.html', {'moods': moods,})

# helper functions
def create_entry(request):
    upi = UserProfileInfo.objects.get(user=request.user)
    if request.method == 'POST':
        date = datetime.datetime.strptime(request.POST.get('date_for'), "%Y-%m-%d")
    else:
        date = datetime.datetime.strptime(request.GET.get('date_picked'), "%m/%d/%Y")

    if Entry.objects.filter(user=upi,date_for=date).exists():
        entry_obj = Entry.objects.get(user=upi,date_for=date)
    else:
        entry_obj = Entry(date_for=date, date_created=datetime.datetime.today(),user=upi)
        entry_obj.save()

    return entry_obj

def populate_mood_form(request, entry_obj):
    if request.method == 'POST':
        if Mood.objects.filter(entry=entry_obj).exists():
            return MoodForm(data=request.POST, instance=Mood.objects.get(entry=entry_obj))
        else:
            return MoodForm(data=request.POST)
    else:
        if Mood.objects.filter(entry=entry_obj).exists():
            return MoodForm(instance=Mood.objects.get(entry=entry_obj))
        else:
            return MoodForm()

def populate_calorie_form(request, entry_obj):
    if request.method == 'POST':
        if Calorie.objects.filter(entry=entry_obj).exists():
            return CalorieForm(data=request.POST, instance=Calorie.objects.get(entry=entry_obj))
        else:
            return CalorieForm(data=request.POST)
    else:
        if Calorie.objects.filter(entry=entry_obj).exists():
            return CalorieForm(instance=Calorie.objects.get(entry=entry_obj))
        else:
            return CalorieForm()
