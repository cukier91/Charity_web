from django.db import models
from django.contrib.auth.models import User



class Type(models.TextChoices):
    foundation = "Fundacja", "Fundacja"
    non_gov_organization = "Organizacja pozarządowa", "Organizacja pozarządowa"
    local_donation = "Zbiórka lokalna", "Zbiórka lokalna"


class CategoryModel(models.Model):
    name = models.CharField(max_length=500)


class InstitutionModel(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=50, choices=Type.choices, default=Type.foundation)
    category = models.ManyToManyField(CategoryModel)


class DonationModel(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(CategoryModel)
    institution = models.ForeignKey(InstitutionModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=20)
    city = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=20)
    pick_up_date = models.DateField(null=False)
    pick_up_time = models.TimeField(null=False)
    pick_up_comment = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

