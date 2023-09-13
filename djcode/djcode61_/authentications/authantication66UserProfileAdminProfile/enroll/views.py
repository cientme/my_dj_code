import django
from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import SignUpform, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm  
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.


# Signup view function.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!')
        form = SignUpform()
        return HttpResponseRedirect('/login/')
    else:
        form = SignUpform()
    return render(request, 'enroll/singup.html', {'form': form})

# Login view function.
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upwd = form.cleaned_data['password']
            user = authenticate(username=uname, password=upwd)
            if user is None:
                login(request, user)
            messages.success(request, 'Logged In Successfully!!')
            return HttpResponseRedirect('/profile/')
    else:
        form = AuthenticationForm()
    return render(request, 'enroll/login.html', {'form': form})

# Profile
def profile(request):
    if request.user:
        if request.method == 'POST':
            form = EditUserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated Successfully!!')
        else:
            form = EditUserProfileForm(instance=request.user)
        return render(request, 'enroll/profile.html', {'name': request.user, 'form': form})
    else:
        return HttpResponseRedirect('/login/')


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# Cgange password with old password.
def user_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
        
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'enroll/changepassword.html', {'form': form})



# Cgange password without old password.
def user_change_password1(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/profile/')
        
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'enroll/changepassword.html', {'form': form})