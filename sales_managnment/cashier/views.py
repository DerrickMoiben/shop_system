from django.shortcuts import render, redirect
from .forms import SingupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

"""This modele is the landing page view when one clicks and opens the software."""
def landing_page(request):
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
                return redirect('cashier-login')
            else:
                messages.error(request, 'They was an error trying to login into the ')

    else:
        form = LoginForm
    return render(request, 'cashier_login.html', {'form': form})