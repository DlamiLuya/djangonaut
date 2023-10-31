from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def logout_view(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
        reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
        reverse('articles:list')
        )
    
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:user_login'))
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('articles:list')
        )


# Define a function that will have a user register their account if they are a new user.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('user_auth:login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)