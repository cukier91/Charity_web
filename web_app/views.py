from django.shortcuts import render, redirect
from django.views.generic import View
from web_app.models import *
from django.db.models import Count, Sum


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
            'foundation_id_3': foundation.filter(type=Type.local_donation)

        }

        return render(request, 'web_app/index.html', context)


class AddDonation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'web_app/form.html')


class Login(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'web_app/login.html')


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'web_app/register.html')
