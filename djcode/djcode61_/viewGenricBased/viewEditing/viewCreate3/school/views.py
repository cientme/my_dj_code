from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .models import Student
from django import forms
from .forms import StudentForm
# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thankyou/'

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class': 'myclass'})
        form.fields['email'].widget = forms.TextInput(attrs={'class': 'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class': 'myclass'})
        return form
 

class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html' 
    success_url = '/thankyou/'

class ThankyouTemplateView(TemplateView):
    template_name = 'school/thankyou.html'
    
