from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.getHome, name='home'),
    path('hive/', views.getHive, name='Hive')
]
