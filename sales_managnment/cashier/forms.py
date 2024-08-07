from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  Sales
from manager.forms import StockForm
from manager.models import Stock


class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class SaleForm(forms.ModelForm):
    calculated_sale_price = forms.FloatField(label='Sale Price', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Sales
        fields = ['stock_item', 'quantity_sold', 'payment_method', 'calculated_sale_price', 'mpesa_code']

    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields['mpesa_code'].required = False

        # Set initial value for calculated_sale_price if instance exists
        if self.instance.pk:
            self.fields['calculated_sale_price'].initial = self.instance.quantity_sold * self.instance.stock_item.product_price
        else:
            self.fields['calculated_sale_price'].initial = 0  # Default initial value

    def clean(self):
        cleaned_data = super().clean()
        stock_item = cleaned_data.get("stock_item")
        quantity_sold = cleaned_data.get("quantity_sold")

        if stock_item and quantity_sold:
            sale_price = quantity_sold * stock_item.product_price
            cleaned_data['calculated_sale_price'] = sale_price
        
        return cleaned_data

    def save(self, commit=True):
        self.instance.sale_price = self.cleaned_data['calculated_sale_price']
        return super(SaleForm, self).save(commit)