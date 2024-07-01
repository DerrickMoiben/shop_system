from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SingupForm, ManagerLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

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
