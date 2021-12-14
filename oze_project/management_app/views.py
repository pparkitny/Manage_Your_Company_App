from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import LoginForm, RegisterForm, EmployeeAddForm, SquadAddForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee, SquadInvestment, POSITION, Squad


class MainSite(View):
    """ This class is represent main site of whole app """
    """ You can choose between 'Login' and 'Register' buttons """
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
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
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        form.is_valid()
        user = authenticate(username=form.cleaned_data['login'],
                            password=form.cleaned_data['password'])  # from django.contrib.auth import authenticate

        if user:  # user is in database
            login(request, user)  # from django.contrib.auth import login
            return redirect('/dashboard/')
        else:  # user is None
            message = 'Błędny login lub hasło'
            return render(request, 'login.html', {'form': form, 'message': message})


class LogoutView(View):
    """ This class redirect logout user to main site"""
    def get(self, request):
        logout(request)  # from django.contrib.auth import logout
        return redirect('/')


class RegisterView(View):
    """ This class is used for new user register """
    def get(self, request):
        form = RegisterForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['login'],
                                            password=form.cleaned_data['password1'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'],
                                            email=form.cleaned_data['email'])
            user.save()
            return redirect('/login/')
        else:
            return render(request, 'add_user.html', {'form': form})


class DashboardView(LoginRequiredMixin, View): # from django.contrib.auth.mixins import LoginRequiredMixin
    """ This class is dashboard for logged users """
    """ You can manage whole app from this place """

    login_url = '/login/'

    def get(self, request):
        return render(request, 'dashboard.html')

    def post(self, request):
        return render(request, 'dashboard.html')


class AddEmployee(LoginRequiredMixin, View):
    """ In this class you can add new employee """

    login_url = '/login/'

    def get(self, request):
        form = EmployeeAddForm()
        return render(request, 'add_employee.html', {'form': form})

    def post(self, request):
        form = EmployeeAddForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            position = form.cleaned_data['position']
            squad = form.cleaned_data['squad']
            # Create new employee
            Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                position=position,
                squad=squad
            )
            return redirect(f'/employees/')
        else:
            return render(request, 'add_employee.html', {'form': form})


class AddSquad(LoginRequiredMixin, View):
    """ In this class you can add new squad """

    login_url = '/login/'

    def get(self, request):
        form = SquadAddForm()
        return render(request, 'add_squad.html', {'form': form})

    def post(self, request):
        form = SquadAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Create new squad
            Squad.objects.create(name=name)
            return redirect(f'/add-squad/')
        else:
            return render(request, 'add_squad.html', {'form': form})


class AddInvestment(LoginRequiredMixin, View):
    """ In this class you can add new investment """

    login_url = '/login/'

    def get(self, request):
        return render(request, 'add_investment.html')

    def post(self, request):
        return render(request, 'add_investment.html')


class Employees(LoginRequiredMixin, View):
    """ In this class you can see list of employees """

    login_url = '/login/'

    def get(self, request):
        workers = Employee.objects.all()
        positions = POSITION
        return render(request, 'employees.html', {'workers': workers, 'positions': positions})

    def post(self, request):
        return render(request, 'employees.html')


class Investments(LoginRequiredMixin, View):
    """ In this class you can see list of investments """

    login_url = '/login/'

    def get(self, request):
        investments = SquadInvestment.objects.all()
        return render(request, 'investments.html', {'investments': investments})

    def post(self, request):
        return render(request, 'investments.html')

