from django.shortcuts import render
from django.http import HttpResponse


def getHome(request): 
    return render(request, 'home/home.html')

def getLogin(request):
    return render(request, 'home/login-form.html')

def getSignup(request):
    return render(request, 'home/signup-form.html')


def getHive(request):
    return render(request, 'main/hive.html')
