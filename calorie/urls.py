from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calories', views.calories, name='calories'),
    path('sleep', views.sleep, name='sleep'),
    path('mood', views.mood, name='mood'),
]
