from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.


def LoginUser(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.object.get(username=username)
        except:
            print('username doesnot exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('username or password is incorrect')

    return render(request, 'users/login-form.html')


def LogoutUser(request):
    logout(request)
    return redirect('login')


def SignupUser(request):
    return render(request, 'users/signup-form.html')
