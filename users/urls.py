from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.getLogin, name='login'),
    path('signup/', views.getSignup, name='signup')
]
