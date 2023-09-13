from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .helpers import send_forget_password_mail
import uuid
from django.core.mail import send_mail 
from django.contrib.auth import (
    authenticate, 
    login, 
    logout, 
    update_session_auth_hash
)
from accounts.forms import ( 
    AccountAuthenticationForm,  
    RegistrationForm, 
    UserPasswordChangeForm,
    UserSetPasswordForm
)
from django.contrib import messages

from accounts.models import Account

# This is User Signup Function.
def signup(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return render(request, 'accounts/already_authenticate.html')
    context = {}

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('signup')
            form.save()
            messages.success(request, "Account Created Successfully !!")
            return redirect('login')

        else:
            email = request.POST.get('email')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            if email == '' or username == '' or password1 == '' or password2 == '':
                messages.success(request, 'Please Fill All Fields Properly.')
                return redirect('signup')

            if Account.objects.filter(email=email).first():
                messages.success(request, 'Email Already Exists.')
                return redirect('signup')

            if Account.objects.filter(username=username).first():
                messages.success(request, 'Username Already Is Taken Choose Different Username.')
                return redirect('signup')
            
            if password1 != password2:
                messages.success(request, 'Password Not Matching...')
                return redirect('signup')

            if username or email in password1:
                messages.success(request, 'Username or email should be not in password')
                return redirect('signup')

            if '1234' or '123456789' or 'abcd' or '=%$#"?><.|!' in password1:               
                messages.success(request, 'Choose secure password')
                return redirect('signup')
    else:
        form = RegistrationForm()
        context = {
            'form':form
        }
    return render(request, 'accounts/signup.html', context)
 


# This is User Login Function.
def user_login(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return render(request, 'accounts/already_authenticate.html')
    context = {}

    if request.method == 'POST':
        form = AccountAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
           
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('post-list')
                
      
    else:
        form = AccountAuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

# This is User Logout Function.
def user_logout(request, *args, **kwargs):
    logout(request)
    return redirect('/')


# Change Password With Old password.
def user_change_password_with_old_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserPasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Change Successfully !!')
                return redirect('profile')
    
        else:
            form =UserPasswordChangeForm(user=request.user)
        return render(request, 'accounts/change_password_with_old_password.html', {'form':form})
    else:
        return redirect('login')

# Change Password Without Old password.

def user_change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserSetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Change Successfully !!')
                return redirect('profile')
    
        else:
            form = UserSetPasswordForm(user=request.user)
        return render(request, 'accounts/change_password.html', {'form':form})
    else:
        return redirect('login')


#forget Password
def forget_password(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            if not Account.objects.filter(username=username).first():
                messages.success(request, f'Not User Found With This Username.')
                return redirect('forget-password')

            user_obj = Account.objects.filter(username=username).first()
            token = str(uuid.uuid4())
            print(token)
            send_forget_password_mail(user_obj.email)
            messages.success(request, 'An email is sent.')
            return redirect('forget-password')

    except Exception as e:
        print(e)
    return render(request, 'accounts/forget_password.html')

