from django.shortcuts import render


def getHome(request):
    return render(request, 'home/home.html')

