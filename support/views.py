# support/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import UpdateRequestStatusForm
from django.contrib.auth.decorators import user_passes_test


@login_required
def dashboard(request):
    all_requests = ServiceRequest.objects.all().order_by('-submitted_at')
    return render(request, 'support/dashboard.html', {'all_requests': all_requests})

@login_required
def update_request_status(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        form = UpdateRequestStatusForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('support:dashboard')  # Corrected the URL name to `support:dashboard`
    else:
        form = UpdateRequestStatusForm(instance=service_request)
    return render(request, 'support/update_status.html', {'form': form, 'request': service_request})

@login_required
def customer_details(request, customer_id):
    from customer.models import Customer
    customer = get_object_or_404(Customer, pk=customer_id)
    requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'support/customer_details.html', {'customer': customer, 'requests': requests})

def home(request):
    return render(request, 'support/support_home.html')


def admin_required(function):
    return user_passes_test(lambda u: u.is_superuser)(function)

@login_required
@admin_required  # Ensure only superusers can access this view
def support_home(request):
    return render(request, 'support/support_home.html')
