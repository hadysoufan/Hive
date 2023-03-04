from django.shortcuts import render

def getHome(request): 
    return render(request, 'home/home.html')

def getHive(request):
    return render(request, 'main/hive.html')
