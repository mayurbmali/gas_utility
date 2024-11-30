# main/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def register(request):
    # Implement your registration logic here (form handling, etc.)
    return render(request, 'register.html')