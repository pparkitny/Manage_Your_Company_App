from django import forms
from django.contrib.auth.models import User
from django.core.validators import URLValidator, validate_email, ValidationError


class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput())


def login_not_taken(login):
    if User.objects.filter(username=login):
        raise ValidationError('Podany login jest zajęty')


class RegisterForm(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     self.fields['login'].widget.attrs.update({
    #         'autocomplete': 'off'
    #     })

    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    login = forms.CharField(label='Login', validators=[login_not_taken])
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput())
    email = forms.CharField(label='Email')


    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidateError('Hasła nie są takie same')
        return cleaned_data
