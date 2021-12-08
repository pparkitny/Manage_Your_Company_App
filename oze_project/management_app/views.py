from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


class MainSite(View):
    """ This class is represent main site of whole app """
    """ You can choose between 'Login' and 'Register' buttons """
    def get(self, request):
        return render(request, 'main.html')

    def post(self, request):
        if request.method == "POST":
            if 'login' in request.POST: # login button click
                return redirect("/login/")
            elif 'register' in request.POST: # register button click
                return redirect("/register/")


class LoginView(View):
    """ This class is used for user login """
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        form.is_valid()
        user = authenticate(username=form.cleaned_data['login'],
                            password=form.cleaned_data['password'])  # from django.contrib.auth import authenticate

        if user:  # user is in database
            message = f'Witaj {user}'
            login(request, user)  # from django.contrib.auth import login
            return render(request, 'login.html', {'form': form, 'message': message})
        else:  # user is None
            message = 'Błędny login lub hasło'
            return render(request, 'login.html', {'form': form, 'message': message})
