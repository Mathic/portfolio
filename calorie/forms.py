# dappx/forms.py
from django import forms
from calorie.models import Calorie, Mood, Setup, Sleep, UserProfileInfo
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

MOOD_RATING = [
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site',)

class SetupForm(forms.ModelForm):
    class Meta():
        model = Setup
        fields = ('first_name', 'last_name', 'height', 'age', 'gender', 'weight')

        widgets = {
            'gender': forms.RadioSelect(attrs={
                'class': 'radio-choices'}, choices=GENDER_CHOICES)
        }

class CalorieForm(forms.ModelForm):
    class Meta():
        model = Calorie
        fields = ('entry_weight', 'calories_in', 'calories_out')

class SleepForm(forms.ModelForm):
    class Meta():
        model = Sleep
        fields = ('time_slept', 'time_awake')

class MoodForm(forms.ModelForm):
    class Meta():
        model = Mood
        fields = ('mood_rating', 'mood_time', 'mood_notes')

        widgets = {
            'mood_rating': forms.RadioSelect(attrs={
                'class': 'radio-choices'}, choices=MOOD_RATING)
        }
