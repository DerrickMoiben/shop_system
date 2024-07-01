from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SingupForm, ManagerLoginForm, StockForm, EmployeeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Stock
from django.shortcuts import get_object_or_404

def admin_dashboard(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The stock was added succefully')
            return redirect('admin-dashboard')
    else:
        form = StockForm()
    return render(request, 'admin_dashboard.html', {'form': form})

def manager_sing_up(request):
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.sucess(request, 'The cashier was Loged in succefully')
            return redirect('manager-login')
    else:
        form = SingupForm()
    return render(request, 'manager_singup.html', {'form': form})

def manager_login(request):
    if request.method == "POST":
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = ManagerLoginForm.cleaned_data.get('password')
            cashier = authenticate(username=username, password=password)
            if cashier:
                login(request, cashier)
                messages.success(request, 'You have login in succefully cashier')
                return redirect('admin-dashboard')
            else:
                messages.error(request, 'They was an error trying to login into the ')

    else:
        form = ManagerLoginForm
    return render(request, 'manager_login.html', {'form': form})

def new_staff(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The employee was added succefully')
            return redirect('new-staff')
    else:
        form = EmployeeForm()
    return render(request, 'new_staff.html', {'form': form})

def all_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'all_stock.html', {'stocks': stocks})

def edit_stock(request, stock_id):
    stock = get_object_or_404(Stock, id = stock_id)

    if request.method == 'POST':
        stock.product_name = request.POST['product_name']
        stock.product_id = request.POST['product_id']
        stock.product_quantity = request.POST['product_quantity']
        stock.product_price = request.POST['product_price']
        stock.save()
        messages.success(request, 'The stock was updated succefully')
        return redirect('all-stock')
    
    return render(request, 'edit_stock.html', {'stock': stock})