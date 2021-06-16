from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, FormView, CreateView

from web_app.forms import CreateUserForm, DonationForm
from web_app.models import DonationModel, InstitutionModel, Type, CategoryModel
from django.db.models import Count, Sum
from django.core.paginator import Paginator
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin


# TODO dodawać możliwość dla funfacji więcej niż jedna kategoria
class LandingPage(View):
    def get(self, request, *args, **kwargs):
        foundation = InstitutionModel.objects.all()
        bags = DonationModel.objects.aggregate(
            total=Sum('quantity'),
            institution=Count('pk')
        ),
        context = {
            'total': bags[0]['total'],
            'institution': bags[0]['institution'],
            'foundation_id_1': foundation.filter(type=Type.foundation),
            'foundation_id_2': foundation.filter(type=Type.non_gov_organization),
            'foundation_id_3': foundation.filter(type=Type.local_donation),


        }

        return render(request, 'web_app/index.html', context)


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request, *args, **kwargs):
        category = InstitutionModel.objects.all()
        form = DonationForm()
        ctx = {
            'category': category,
            'form': form,
        }
        return render(request, 'web_app/form.html', ctx)

    def post(self, request, *args, **kwargs):
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('register_page')

class Login(LoginView):
    template_name = 'web_app/login.html'
    redirect_authenticated_user = LandingPage

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm
        return render(request, 'web_app/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return redirect('register_page')


class Logout(LogoutView):
    next_page = '/login'


class Register(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'web_app/register.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            error = "Niepowodzenie, spróbuj ponownie"
            return render(request, 'web_app/register.html', {'form': CreateUserForm, 'error': error})


