from django import forms
from django.contrib.auth.forms import UserCreationForm
from web_app.models import User


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Podaj imię.. "}),
            'last_name': forms.TextInput(attrs={'placeholder': "Podaj nazwisko.."}),
            'email': forms.EmailInput(attrs={'placeholder': "e-mail.."}),

        }

