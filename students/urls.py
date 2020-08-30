"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views as stud_views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('login/', auth_views.LoginView.as_view(
            template_name='students/logs/login.html'
        ), name='stud_login'),
    #path('user_profile/', stud_views.Profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(
            template_name='students/logs/logout.html'
        ), name='stud_logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='students/logs/password_reset.html'
         ),
         name='stud_password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='students/logs/password_reset_done.html'
         ),
         name='stud_password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='students/logs/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('stud_password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='students/logs/password_reset_complete.html'
         ),
         name='stud_password_reset_complete'),
]
