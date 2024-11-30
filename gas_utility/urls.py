# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from gas_utility import views 
from django.contrib.auth import views as auth_views
from customer.views import register 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls', namespace='customer')),  # Customer module routes
    path('support/', include('support.urls', namespace='support')),  # Support module routes
    path('', views.home, name='home'), # Redirect root to customer home
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
