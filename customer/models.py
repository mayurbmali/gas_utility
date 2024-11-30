#customer/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class Customer(AbstractUser):
    address = models.TextField(blank=True, null=True)  # Optional for flexibility
    contact_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
        help_text="Enter a valid phone number."
    )

    def __str__(self):
        return f"{self.username} ({self.contact_number})"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
