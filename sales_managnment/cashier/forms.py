from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Sale


class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SaleItemForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1)
    

class SaleForm(forms.Form):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('Mpesa', 'Mpesa'),
    ]

    item = forms.CharField(widget=forms.HiddenInput) #This will hold JSON data of the SaleItemForm
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES)
    payment_code = forms.CharField(max_length=100) #This will hold the Mpesa code  

    def clean(self):
        cleaned_data = super().clean()
        item = cleaned_data.get('item')
        payment_method = cleaned_data.get('payment_method')
        payment_code = cleaned_data.get('payment_code')

        if not item:
            raise forms.ValidationError('Please add at least one item to the sale')
        if payment_method == 'Mpesa' and not payment_code:
            raise forms.ValidationError('Please provide the Mpesa code')
        return cleaned_data