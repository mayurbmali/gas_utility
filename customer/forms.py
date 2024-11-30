#customer/forms.py

from django import forms
from support.models import ServiceRequest
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description', 'attachment']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        help_texts = {
            'service_type': 'Select the type of service you require.',
            'description': 'Provide detailed information about your request.',
            'attachment': 'You may upload relevant files or images (optional).',
        }



class CustomerRegistrationForm(UserCreationForm):
    address = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text="Enter your complete address."
    )
    contact_number = forms.CharField(
        required=True,
        help_text="Enter a valid phone number."
    )

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2', 'address', 'contact_number']