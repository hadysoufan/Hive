from django.shortcuts import render
from django.http import HttpResponse


def getHome(request):
    return render(request, 'index.html')


def getHive(request):
    return render(request, 'hive.html')
