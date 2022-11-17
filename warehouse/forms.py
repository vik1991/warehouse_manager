from django import forms
from django.core.validators import RegexValidator, EmailValidator


class LoginForm(forms.Form):
    email = forms.EmailField()
