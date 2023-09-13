from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView

# Create your views here.

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student.html'   # custom template name
    context_object_name = 'stu'             # custom context name
    pk_url_kwarg = 'naufil'                      # custom pk or id name