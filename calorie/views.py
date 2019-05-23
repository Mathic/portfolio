from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView

from calorie.forms import *
from calorie.models import Calorie, Entry, Setup, UserProfileInfo

import datetime

# Create your views here.
def index(request):
    return render(request, 'calorie/index.html', {'nbar': 'home'})

@login_required
def calories(request):
    upi = UserProfileInfo.objects.get(user=request.user)
    today = datetime.datetime.today()
    entry_exists = Entry.objects.filter(date_for=today).exists()
    
    if entry_exists:
        obj = Calorie.objects.get(entry=Entry.objects.get(date_for=today))
        print(obj)

    if request.method == 'POST':
        if entry_exists:
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
        if entry_exists:
            calorie_form = CalorieForm(instance=obj)
        else:
            calorie_form = CalorieForm()

    return render(request, 'calorie/calories.html', {'nbar': 'calories', 'calorie_form': calorie_form})

@login_required
def sleep(request):
    return render(request, 'calorie/sleep.html', {'nbar': 'sleep'})

@login_required
def mood(request):
    return render(request, 'calorie/mood.html', {'nbar': 'mood'})

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
