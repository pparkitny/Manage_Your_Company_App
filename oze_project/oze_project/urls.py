"""oze_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from management_app.views import MainSiteView, LoginView, LogoutView, RegisterView, \
    DashboardView, AddEmployeeView, AddSquadView, AddInvestmentView,\
    EmployeesView, InvestmentsView, SquadsView, CalendarView,\
    ModifyEmployeeView, ModifySquadView, ModifyInvestmentView, SelectedDayFromCalendarView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainSiteView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('dashboard/', DashboardView.as_view()),
    path('add-employee/', AddEmployeeView.as_view()),
    path('add-squad/', AddSquadView.as_view()),
    path('add-investment/', AddInvestmentView.as_view()),
    path('employees/', EmployeesView.as_view()),
    path('investments/', InvestmentsView.as_view()),
    path('squads/', SquadsView.as_view()),
    path('calendar/', CalendarView.as_view()),
    path('employee/modify/<id>/', ModifyEmployeeView.as_view()),
    path('squad/modify/<id>/', ModifySquadView.as_view()),
    path('investment/modify/<id>/', ModifyInvestmentView.as_view()),
    path('calendar/<day_name>/<month_name>/<year_name>/', SelectedDayFromCalendarView.as_view())
]
