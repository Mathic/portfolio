from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calories', views.calories, name='calories'),
    path('sleep', views.sleep, name='sleep'),
    path('mood', views.mood, name='mood'),
    path('profile', views.profile, name='profile'),

    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='logout'),
]
