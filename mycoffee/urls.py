from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    
    path('', views.homepage, name=""),
    
    path('accounts/login/register/', views.register, name="register"),
    
    path('login/', views.my_login, name="login"),
    
    path('accounts/profile/', views.dashboard, name="dashboard"),
    
    path('accounts/logout/', views.logout, name="logout"),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="cafe/password_reset_form.html"),
         name="reset_password"),
    
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="cafe/password_reset_done.html"),
         name="reset_password_done"),
   
    path('accounts/reset/MTI/set-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "cafe/password_reset_confirm.html"),
         name="password_reset_confirm"),
   
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="cafe/password_reset_complete.html"),
         name="reset_password_complete"),
]



