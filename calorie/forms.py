# dappx/forms.py
from django import forms
from calorie.models import Calorie, Setup, UserProfileInfo
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
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

class SetupForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    height = forms.DecimalField(max_digits=6, decimal_places=3)
    age = forms.DecimalField(max_digits=3, decimal_places=0)
    gender = forms.CharField(widget=forms.RadioSelect(attrs={'class': 'gender-choice'}, choices=GENDER_CHOICES))
    weight = forms.DecimalField(max_digits=6, decimal_places=3)

class SetupForm(forms.ModelForm):
    class Meta():
        model = Setup
        fields = ('first_name', 'last_name', 'height', 'age', 'gender', 'weight')

class CalorieForm(forms.Form):
    entry_weight = forms.DecimalField(max_digits=6, decimal_places=3)
    calories_in = forms.DecimalField(max_digits=6, decimal_places=2)
    calories_out = forms.DecimalField(max_digits=6, decimal_places=2)

class CalorieForm(forms.ModelForm):
    class Meta():
        model = Calorie
        fields = ('entry_weight', 'calories_in', 'calories_out')
