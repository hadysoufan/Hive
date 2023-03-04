from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True,
                             help_text='Required. Enter a valid email address.')
    username = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    password1 = forms.CharField(
        widget=forms.PasswordInput, help_text='Required. Enter a strong password.')
    password2 = forms.CharField(
        widget=forms.PasswordInput, help_text='Required. Confirm password.')

    class Meta:
        model = User
        fields = ('name', 'email', 'username', 'password1', 'password2')
