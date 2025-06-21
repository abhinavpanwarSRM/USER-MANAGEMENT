# auth_system/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth_system/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth_system/logout.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]