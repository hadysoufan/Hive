from django.shortcuts import render

# Create your views here.


def getHive(request):
    return render(request, 'hive/hive.html')

def getUserProfile(request):
    return render(request, 'hive/profiles.html')