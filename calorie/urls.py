from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calories', views.calories, name='calories'),
    path('sleep', views.sleep, name='sleep'),
    path('mood', views.mood, name='mood'),
    path('profile', views.profile, name='profile'),

    # authentication
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='logout'),

    # ajax requests
    path('ajax/load-calorie', views.load_calorie, name='ajax_load_calorie'),
    path('ajax/load-sleep', views.load_sleep, name='ajax_load_sleep'),
    path('ajax/load-mood', views.load_mood, name='ajax_load_mood'),
]
