from django.shortcuts import render, redirect
from django.views.generic import View


class LandingPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'web_app/index.html')


class AddDonation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'web_app/form.html')


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'web_app/login.html')


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'web_app/register.html')

