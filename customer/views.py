#customer/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from support.models import ServiceRequest
from .forms import ServiceRequestForm
from .forms import CustomerRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "There was an issue with your registration. Please check the form.")
    else:
        form = CustomerRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            messages.success(request, "Your service request has been submitted successfully.")
            return redirect('customer:track_request')
        else:
            messages.error(request, "There was an issue with your submission. Please check the form.")
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/service_request.html', {'form': form})

@login_required
def track_request(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    if not requests:
        messages.info(request, "You have no service requests at the moment.")
    return render(request, 'customer/track_request.html', {'requests': requests})

@login_required
def account_info(request):
    return render(request, 'customer/account_info.html')

def home(request):
    return render(request, 'customer/customer_home.html')
