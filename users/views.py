from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm


def LoginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('hive')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username:
            messages.error(request, 'Please enter your username')
            return redirect('login')
        if not password:
            messages.error(request, 'Please enter your password')
            return redirect('login')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')
            return redirect('login')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print('Login successful')
            return redirect('hive')
        else:
            error_msg = 'Username or password is incorrect'
            messages.error(request, error_msg)
            print(error_msg)
            return redirect('login')

    return render(request, 'users/login-form.html')


def LogoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


def SignupUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()

                messages.success(request, 'User account was created')

                login(request, user)

                print('New user created: ', user.username)

                return redirect('hive')
            else:
                messages.error(
                    request, 'Passwords do not match. Please try again.')
                print('Passwords do not match')
        else:
            messages.error(request, 'An error has occurred. Please try again.')
            print('Form is invalid: ', form.errors)

    context = {'page': page, 'form': form}

    return render(request, 'users/signup-form.html', context)
