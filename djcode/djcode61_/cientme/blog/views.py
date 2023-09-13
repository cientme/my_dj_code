from django.shortcuts import render, HttpResponseRedirect
from blog import forms
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# Signup view function.
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'SignedUp Successfully!!!')
        form = SignupForm()
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form})

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
    return render(request, 'blog/login.html', {'form': form})


def profile(request):
    return render(request, 'blog/profile.html', {'name': request.user})

# Logout view function.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')