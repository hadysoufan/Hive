from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.getHome, name='home'),
    path('user/<str:pk>', views.getUser, name='user')
]
