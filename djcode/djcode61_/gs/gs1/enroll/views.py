from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import EditUserProfileForm
from enroll.forms import SignUpform, EditUserProfileForm, EditAdminProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash



# Create your views here.

# this is Signup function.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'SignedUp Successfully!!')
        form = SignUpform()
    else:
        form = SignUpform()
    return render(request, 'enroll/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upwd = form.cleaned_data['password']
            user = authenticate(username=uname, password=upwd)
            login(request, user)
            messages.success(request, 'Logged In Successfully!!!')
        return HttpResponseRedirect('/profile/')
    else:
        form = AuthenticationForm()
    return render(request, 'enroll/login.html', {'form': form})

# User profile view function.
def user_profile(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login/')
        
    else:
        return render(request, 'enroll/profile.html', {'name': request.user})


# User logout view function.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# change password with old password.
def user_change_password(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login/')

    elif request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/profile/')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'enroll/changepass.html', {'form': form})


# Change password without odl password.
def user_change_password1(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login/')
    elif request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/profile/')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'enroll/changepass1.html', {'form': form})
    
# Update profile view function.
def updateProfile(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/profile/')
    else:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                form = EditUserProfileForm(request.POST ,instance=request.user)
                users = None
            if form.is_valid():
                messages.success(request, 'Profile Updated')
                form.save()
        else:
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                form = EditUserProfileForm(request.POST)
                users = None
    
    return render(request, 'enroll/updateProfile.html', {'form': form, 'users': users})


# User detail view function.
def user_detail(request, id):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login/')
    else:
        pi = User.objects.get(pk=id)
        form = EditAdminProfileForm(instance=pi)
        return render(request, 'enroll/userdetail.html', {'form': form, 'name':request.user.username})