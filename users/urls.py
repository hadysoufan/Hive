from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('signup/', views.SignupUser, name='signup')
]
