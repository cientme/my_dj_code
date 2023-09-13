from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import SignUpform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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
        return render(request, 'enroll/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')