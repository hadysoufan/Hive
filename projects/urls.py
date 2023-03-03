from django.urls import path


urlpatterns = [
    path('home/', getHome, name='home'),
    path('user/<str:pk>', getUser, name='home')
]