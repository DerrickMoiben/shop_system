from django.shortcuts import render, redirect
from .forms import SingupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from .models import Sales
from .forms import SaleForm
from django.http import JsonResponse
from manager.forms import StockForm
from manager.models import Stock

def landing_page(request):
    """This modele is the landing page view when one clicks and opens the software."""
    return render(request, 'landing_page.html')



def cashier_sing_up(request):
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.sucess(request, 'The cashier was Loged in succefully')
            return redirect('cashier-login')
    else:
        form = SingupForm()
    return render(request, 'cashier_singup.html', {'form': form})

def cashier_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            cashier = authenticate(username=username, password=password)
            if cashier:
                login(request, cashier)
                messages.success(request, 'You have login in succefully cashier')
                return redirect('cashier-dashboard')
            else:
                messages.error(request, 'They was an error trying to login into the ')

    else:
        form = LoginForm
    return render(request, 'cashier_login.html', {'form': form})

from django.contrib import messages

def cashier_dashboard(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            if sale.payment_method == 'Mpesa' and not sale.mpesa_code:
                form.add_error('mpesa_code', 'Mpesa code is required for Mpesa payments.')
            else:
                # Retrieve the stock item instance
                stock_item = sale.stock_item
                
                # Check stock availability
                if stock_item.product_quantity < sale.quantity_sold:
                    form.add_error('quantity_sold', 'There is not enough stock to complete this sale.')
                    messages.error(request, 'There is not enough stock to complete this sale.')
                else:
                    sale.save()
                    messages.success(request, 'Sale was successful.')
                    return redirect('stock_add')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SaleForm()

    return render(request, 'cashier_dashboard.html', {'form': form})


def sales_summary(request):
    sales = Sales.objects.all()
    return render(request, 'sales_summary.html', {'sales': sales})