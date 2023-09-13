from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student.html'   # custom template name
   

class StudentListView(ListView):
    model = Student