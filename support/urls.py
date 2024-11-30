# support/urls.py

from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('', views.home, name='support_home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update-status/<int:pk>/', views.update_request_status, name='update_request_status'),
    path('customer-details/<int:customer_id>/', views.customer_details, name='customer_details'),
]
