from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome, name='home'),
    path('login/', views.getLogin, name='login'),
    path('hive/', views.getHive, name='Hive'),
]
