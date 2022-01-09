from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee, SquadInvestment, POSITION, Squad, Investment, TYPES_OF_INVESTMENT,\
    DayName, InvestmentEachDate, EachDate
from .forms import LoginForm, RegisterForm, EmployeeAddForm, SquadAddForm, InvestmentAddForm
from datetime import datetime


class MainSiteView(View):
    """ This class is represent main site of whole app """
    """ You can choose between 'Login' and 'Register' buttons """
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        return render(request, 'main.html')

    def post(self, request):
        if request.method == "POST":
            if 'login' in request.POST:  # login button click
                return redirect("/login/")
            elif 'register' in request.POST:  # register button click
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
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])  # from django.contrib.auth import authenticate

        if user:  # user is in database
            login(request, user)  # from django.contrib.auth import login
            return redirect('/dashboard/')
        else:  # user is None
            message = 'Wrong login or password'
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


class DashboardView(LoginRequiredMixin, View):  # from django.contrib.auth.mixins import LoginRequiredMixin
    """ This class is dashboard for logged users """
    """ You can manage whole app from this place """

    login_url = '/login/'

    def get(self, request):
        return render(request, 'dashboard.html')

    def post(self, request):
        return render(request, 'dashboard.html')


class AddEmployeeView(LoginRequiredMixin, View):
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


class AddSquadView(LoginRequiredMixin, View):
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


class AddInvestmentView(LoginRequiredMixin, View):
    """ In this class you can add new investment """

    login_url = '/login/'

    def get(self, request):
        form = InvestmentAddForm()
        return render(request, 'add_investment.html', {'form': form})

    def post(self, request):
        form = InvestmentAddForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            street_name = form.cleaned_data['street_name']
            city_name = form.cleaned_data['city_name']
            zip_code = form.cleaned_data['zip_code']
            type_of_investment = form.cleaned_data['type_of_investment']
            # Create new investment
            investment = Investment.objects.create(
                first_name=first_name,
                last_name=last_name,
                street_name=street_name,
                city_name=city_name,
                zip_code=zip_code,
                type_of_investment=type_of_investment
            )
            SquadInvestment.objects.create(
                investment=investment
            )
            return redirect(f'/investments/')
        else:
            return render(request, 'add_investment.html', {'form': form})


class EmployeesView(LoginRequiredMixin, View):
    """ In this class you can see list of employees """

    login_url = '/login/'

    def get(self, request):
        workers = Employee.objects.all().order_by('id')
        positions = POSITION
        return render(request, 'employees.html', {'workers': workers, 'positions': positions})

    def post(self, request):
        return render(request, 'employees.html')


class InvestmentsView(LoginRequiredMixin, View):
    """ In this class you can see list of investments """

    login_url = '/login/'

    def get(self, request):
        investments = SquadInvestment.objects.all().order_by('id')
        types_of_investment = TYPES_OF_INVESTMENT
        return render(request, 'investments.html', {'investments': investments,
                                                    'types_of_investment': types_of_investment})

    def post(self, request):
        return render(request, 'investments.html')


class SquadsView(LoginRequiredMixin, View):
    """ In this class you can see list of investments """

    login_url = '/login/'

    def get(self, request):
        squads = Squad.objects.all().order_by('id')
        return render(request, 'squads.html', {'squads': squads})

    def post(self, request):
        return render(request, 'squads.html')


class CalendarView(LoginRequiredMixin, View):
    """ In this class you can see calendar """

    login_url = '/login/'

    def get(self, request):
        day_name = DayName.objects.all().order_by('id')
        currentMonth = datetime.now().strftime('%B')
        all_dates = EachDate.objects.all().filter(month_name=12).filter(year_name=2021).order_by('id')
        return render(request, 'calendar.html', {'day_name': day_name,
                                                 'currentMonth': currentMonth,
                                                 'all_dates': all_dates})

    def post(self, request):
        return render(request, 'calendar.html')


class SelectedDayFromCalendarView(LoginRequiredMixin, View):
    """ In this class you can see selected day from the calendar """

    login_url = '/login/'

    def get(self, request, day_name, month_name, year_name):
        try:
            selectedDay = EachDate.objects.get(day_name=day_name, month_name=month_name, year_name=year_name)
        except Exception:
            raise Http404("Day not found")
        return render(request, 'selected_day.html', {'selectedDay': selectedDay})

    def post(self, request, id):
        return redirect(f'/calendar/')


class ModifyEmployeeView(LoginRequiredMixin, View):
    """ In this class you can add modify each employee """

    login_url = '/login/'

    def get(self, request, id):
        positions = POSITION
        squads = Squad.objects.all()
        try:
            employee = Employee.objects.get(id=id)
        except Exception:
            raise Http404("Employee not found")
        return render(request, 'modify_employee.html', {'employee': employee,
                                                        'positions': positions,
                                                        'squads': squads})

    def post(self, request, id):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        position = request.POST.get('position')
        squad_name = request.POST.get('squad')
        squad = Squad.objects.get(name=squad_name)
        new = ""
        for pos in POSITION:
            if position == pos[1]:
                new = str(pos[0])
        # Update employee
        Employee.objects.filter(id=id).update(
            first_name=first_name,
            last_name=last_name,
            position=new,
            squad=squad
        )
        return redirect(f'/employees/')


class ModifySquadView(LoginRequiredMixin, View):
    """ In this class you can add modify each squad """

    login_url = '/login/'

    def get(self, request, id):
        try:
            squad = Squad.objects.get(id=id)
        except Exception:
            raise Http404("Squad not found")
        return render(request, 'modify_squad.html', {'squad': squad})

    def post(self, request, id):
        name = request.POST.get('name')
        # Update squad
        Squad.objects.filter(id=id).update(
            name=name
        )
        return redirect(f'/squads/')


class ModifyInvestmentView(LoginRequiredMixin, View):
    """ In this class you can add modify each investment """

    login_url = '/login/'

    def get(self, request, id):
        type_of_investments = TYPES_OF_INVESTMENT
        try:
            investment = Investment.objects.get(id=id)
        except Exception:
            raise Http404("Investment not found")
        return render(request, 'modify_investment.html', {'investment': investment,
                                                          'type_of_investments': type_of_investments})

    def post(self, request, id):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        street_name = request.POST.get('street_name')
        city_name = request.POST.get('city_name')
        zip_code = request.POST.get('zip_code')
        type_of_investment = request.POST.get('type_of_investment')
        new = ""
        for investment in TYPES_OF_INVESTMENT:
            if type_of_investment == investment[1]:
                new = str(investment[0])
        #  Update employee
        Investment.objects.filter(id=id).update(
            first_name=first_name,
            last_name=last_name,
            street_name=street_name,
            city_name=city_name,
            zip_code=zip_code,
            type_of_investment=new
        )
        return redirect(f'/investments/')
