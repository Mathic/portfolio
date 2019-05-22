from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Setup)
admin.site.register(Entry)
admin.site.register(Calorie)
admin.site.register(Sleep)
admin.site.register(Exercise)
