#support/forms.py

from django import forms
from .models import ServiceRequest

class UpdateRequestStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
