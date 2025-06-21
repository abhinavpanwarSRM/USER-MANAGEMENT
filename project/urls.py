from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/')),  # Add this line
    path('', include('auth_system.urls')),
]