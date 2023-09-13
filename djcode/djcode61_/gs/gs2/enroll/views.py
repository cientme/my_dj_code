from email.headerregistry import Group
from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import EditUserProfileForm
from enroll.forms import SignUpform, EditUserProfileForm, EditAdminProfileForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash



# Create your views here.

# this is Signup function.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            messages.success(request, 'SignedUp Successfully!!')
            user = form.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
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
        return HttpResponseRedirect('/dashboard/')
    else:
        form = AuthenticationForm()
    return render(request, 'enroll/login.html', {'form': form})

# User Dahsboard view function.
def user_dashboard(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login/')
        
    else:
        return render(request, 'enroll/dashboard.html', {'name': request.user.username})


# User logout view function.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def index(request):
    if request.user.is_authenticated:
        print('Logged In')
    else:
        print('Not Logged In')
    return HttpResponseRedirect('/login/')