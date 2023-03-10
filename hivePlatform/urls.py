from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHive, name='hive'),
    path('edit-profile/', views.getSettings, name='edit-profile'),
    path('profile/', views.getUserProfile, name='profile')
]
