from django import forms
from django.contrib.auth.models import User
from django.core.validators import URLValidator, validate_email, ValidationError


class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


