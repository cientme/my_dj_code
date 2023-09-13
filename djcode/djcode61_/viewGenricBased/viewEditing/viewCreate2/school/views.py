from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Student

# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    # success_url = '/thankyou/'
    template_name = 'school/sform.html'

class ThankyouTemplateView(TemplateView):
    template_name = 'school/thankyou.html'
    
class StudentDetailView(DetailView):
    model = Student