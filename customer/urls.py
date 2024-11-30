#customer/urls.py

from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.home, name='customer_home'),  # Root path for customer app
    path('submit-request/', views.submit_request, name='submit_request'),
    path('track-request/', views.track_request, name='track_request'),
    path('account-info/', views.account_info, name='account_info'),
]
