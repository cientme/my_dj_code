from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic.base import TemplateView
from myapp.forms import LoginForm

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'myapp/home.html'

class DashboardTemplateView(TemplateView):
    template_name = 'myapp/dashboard.html'

class MyLoginView(LoginView):
    template_name = 'myapp/login.html'
    authentication_form = LoginForm
    

class MyLogoutView(LogoutView):
    template_name = 'myapp/logout.html'

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'myapp/changepass.html'
    success_url = '/changepassdone/'

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'myapp/changepassdone.html'

