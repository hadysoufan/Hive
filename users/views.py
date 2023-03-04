from django.shortcuts import render

# Create your views here.


def getLogin(request):
    return render(request, 'users/login-form.html')


def getSignup(request):
    return render(request, 'users/signup-form.html')
