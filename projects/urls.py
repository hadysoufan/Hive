from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome, name='home'),
    path('login/', views.getLogin, name='login-form'),
    path('sigup/', views.getSignup, name='signup-form'),
    path('hive/', views.getHive, name='Hive')
]
