from django.shortcuts import render, redirect
from .forms import SingupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from .models import Product, Sale
from .forms import SaleForm, SaleItemForm
from django.http import JsonResponse

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

def cashier_dashboard(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            item = json.loads(form.cleaned_data.get('item'))
            payment_method = form.cleaned_data.get('payment_method')
            payment_code = form.cleaned_data.get('payment_code')
            total_price = 0

            for i in item:
                product = Product.objects.get(id=i['product'])
                quantity = i['quantity']
                if quantity > product.product_quantity:
                    messages.error(request, f'The quantity of {product.product_name} is not enough')
                    return redirect('cashier-dashboard')
                total_price += product.product_price * quantity
                product.product_quantity -= quantity
                product.save()
                
            for i in item:
                product = Product.objects.get(id=i['product'])
                quantity = i['quantity']
                sale = Sale(product=product, quantity=quantity, total_price=total_price, payment_method=payment_method)
                sale.save()

            messages.success(request, 'The sale was made successfully')
            return redirect('cashier-dashboard')
    else:
        form = SaleForm()
    items = SaleItemForm()
    return render(request, 'cashier_dashboard.html', {'form': form, 'items': items})

def add_sale_item(request):
    if request.method == 'POST':
        form = SaleItemForm(request.POST)
        if form.is_valid():
            return JsonResponse({'status': 'success', 'data': form.cleaned_data})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})

    return JsonResponse({'status': 'error', 'errors': 'Invalid request method'})