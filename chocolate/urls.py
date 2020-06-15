from django.urls import path

from . import views

urlpatterns = [
    path('', views.chocolate, name='chocolate'),
    path('beans', views.beans, name='beans'),
    path('read', views.first_time, name='data'),
]
