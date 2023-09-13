from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .forms import StudentForm
from .models import Student

# Create your views here.


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'
 
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'School/student_form.html'
    success_url = '/thanksupdate/'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'school/studentdelete.html'
    success_url = '/thanksdelete/'

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanksupdate.html'

class ThanksDeleteTemplateView(TemplateView):
    template_name = 'school/thanksdelete.html'