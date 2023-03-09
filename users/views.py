from django.contrib.auth import login
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
            username = form.cleaned_data.get('username').lower()
            email = form.cleaned_data.get('email').lower()
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                form.add_error(
                    'username', 'Username is already taken. Please choose a different username.')
            # Check if email already exists
            if User.objects.filter(email=email).exists():
                form.add_error(
                    'email', 'An account with this email already exists. Please use a different email.')
            if password1 != password2:
                form.add_error(
                    'password2', 'Passwords do not match. Please try again.')
            if form.errors:
                error_messages = ''
                for field, errors in form.errors.items():
                    for error in errors:
                        error_messages += f'{field.capitalize()}: {error}<br>'
                messages.error(
                    request, f'An error has occurred. Please fix the following errors:<br>{error_messages}')
            else:
                user = form.save(commit=False)
                user.username = username
                user.email = email
                user.save()
                messages.success(request, 'User account was created')
                login(request, user)
                print('New user created: ', user.username)
                return redirect('hive')
    context = {'page': page, 'form': form}
    return render(request, 'users/signup-form.html', context)
