from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    #return HttpResponse('home')
    return render(request, 'authentication/login.html')
    

def about(request):
    return render(request, 'about.html')