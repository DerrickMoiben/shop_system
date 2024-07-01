
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class ManagerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)