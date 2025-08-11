from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    # Redirect to the portfolio app's home page instead of showing simple welcome message
    return redirect('portfolio:home')

def about(request):
    # Redirect to the portfolio app's about page
    return redirect('portfolio:about')
