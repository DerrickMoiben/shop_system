
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Stock, Employee


class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class ManagerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product_name', 'product_id', 'product_quantity', 'product_price']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_id', 'employee_salary', 'employee_phone', 'employee_national_id']
