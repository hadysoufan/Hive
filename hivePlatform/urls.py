from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHive, name='hive'),
    path('profile/', views.getUserProfile, name='profile')
]
