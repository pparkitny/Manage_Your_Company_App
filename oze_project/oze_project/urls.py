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

from management_app.views import MainSite, LoginView, LogoutView, RegisterView, \
    DashboardView, AddEmployee, AddSquad, AddInvestment,\
    Employees, Investments
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainSite.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('dashboard/', DashboardView.as_view()),
    path('add-employee/', AddEmployee.as_view()),
    path('add-squad/', AddSquad.as_view()),
    path('add-investment/', AddInvestment.as_view()),
    path('employees/', Employees.as_view()),
    path('investments/', Investments.as_view())
]
