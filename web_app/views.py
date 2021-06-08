from django.shortcuts import render, redirect
from django.views.generic import View
from web_app.models import *
from django.db.models import Count, Q


class LandingPage(View):
    def get(self, request, *args, **kwargs):
        all_bags = DonationModel.objects.all()
        total_bags = 0
        for bag in all_bags:
            total_bags += bag.quantity
        institutions = InstitutionModel.objects.all()
        elements_to_count = 0
        for institution in institutions:
            if len(DonationModel.objects.filter(quantity__gt=0, institution_id=institution.id)) is not 0:
                elements_to_count += 1
        context = {
            'institution': elements_to_count,
            'total': total_bags,
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
