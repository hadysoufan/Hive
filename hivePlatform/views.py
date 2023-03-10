from django.shortcuts import render

# Create your views here.


def getHive(request):
    return render(request, 'hive/hive.html')


def getSettings(request):
    return render(request, 'hive/settings.html')


def getUserProfile(request):
    return render(request, 'hive/profiles.html')
