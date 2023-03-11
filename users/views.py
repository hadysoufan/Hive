from .models import Profile
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile, Post
from .signals import profile_updated


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
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username').lower()
            user.save()

            messages.success(request, 'User account was created')
            login(request, user)
            return redirect('hive')

        else:
            for error in form.errors.values():
                messages.error(request, error)

    context = {'page': page, 'form': form}
    return render(request, 'users/signup-form.html', context)


def editAccount(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('hive')

    context = {'form': form}
    return render(request, 'users/profile-form.html', context)


def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST.get['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('hive')

    else:
        return redirect('hive')
