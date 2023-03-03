from django.shortcuts import render
from django.http import HttpResponse


def getHome(request):
    return HttpResponse("Hello, world. You're at the home page.")


def getUser(request, pk):
    return HttpResponse('Hello world from user' + ' ' + str(pk))
