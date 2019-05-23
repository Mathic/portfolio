from django.urls import path

from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]
