from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm, JourneyForm
from .models import *
from django.db.models import Sum

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account for ' + user + ' was successfully created.')
                return redirect('login')


        context = {'form': form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Invalid Username or Password')
                
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):

    journeys = Journey.objects.all()


    total_emissions = 0
    for i in journeys:
        duration = i.duration_hours * 60 + i.duration_minutes
        total_emissions += duration * i.transportation.carbon_price

    context = {'journeys': journeys, 'total_emissions': total_emissions}
    return render(request, 'accounts/dashboard.html', context)

