from django.shortcuts import render , redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import SetPasswordForm

# Authentication
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login, logout


# CUSTOM PASSWORD

def custom_password_reset_confirm(request, uidb64=None, token=None):
    
    assert uidb64 is not None and token is not None  # checked by URLconf
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # Token is valid, proceed with password reset
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                login(request, user)
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
        return render(request, 'cafe/password_reset_confirm.html', {'form': form})
    else:
        # Log the issue and return an error
        return HttpResponse('Password reset link is invalid or has expired')



# HOMEPAGE
def homepage(request):
    
    return render(request, 'cafe/index.html')

def home(request):
 return render(request, 'home.html',)


#REGISTER
def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        
        form = CreateUserForm(request.POST) 
        
        if form.is_valid():
            
            form.save()
            
            return redirect ("login")
    
    
    context = {'registrationform':form}
    
    return render(request, 'registration/register.html',context=context)


#LOGIN
def my_login(request):

    form = LoginForm()
    
    if request.method == "POST":
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                auth.login(request, user)
                
                return redirect("dashboard")
            
    context = {'loginform' :form}
    
    return render(request, 'registration/login.html', context=context)


#DASHBOARD
@login_required(login_url="login")
def dashboard(request):
    
    return render(request, 'registration/dashboard.html')


#LOGOUT
def logout(request):
    
    auth.logout(request)
    
    return redirect("login")


