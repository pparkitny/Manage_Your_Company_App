from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect


class MainSite(View):
    def get(self, request):
        return render(request, 'main.html')

