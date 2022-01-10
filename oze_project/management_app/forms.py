from django import forms
from django.contrib.auth.models import User
from django.core.validators import URLValidator, validate_email, ValidationError
from .models import Squad, POSITION, Investment, TYPES_OF_INVESTMENT, SquadInvestment


class LoginForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


def login_not_taken(login):
    if User.objects.filter(username=login):
        raise ValidationError('This login is taken!')


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    login = forms.CharField(label='Login', validators=[login_not_taken])
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())
    email = forms.CharField(label='Email')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidateError('Passwords are different!')
        return cleaned_data


class EmployeeAddForm(forms.Form):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    position = forms.ChoiceField(label='Position', choices=POSITION)
    squad = forms.ModelChoiceField(label='Squad', queryset=Squad.objects.all())


def squad_name_not_taken(name):
    if Squad.objects.filter(name=name):
        raise ValidationError('This name is taken!')


class SquadAddForm(forms.Form):
    name = forms.CharField(label='Squad name', validators=[squad_name_not_taken])


class InvestmentAddForm(forms.Form):
    first_name = forms.CharField(label='Investor first name')
    last_name = forms.CharField(label='Investor last name')
    street_name = forms.CharField(label='Street and number')
    city_name = forms.CharField(label='City')
    zip_code = forms.CharField(label='Zip-code')
    type_of_investment = forms.ChoiceField(choices=TYPES_OF_INVESTMENT, label='Type of investment')
