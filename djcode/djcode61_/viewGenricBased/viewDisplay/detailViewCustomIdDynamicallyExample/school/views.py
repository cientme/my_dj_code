from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student.html'   # custom template name
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_student"] = self.model.objects.all().order_by('name')
        return context
    

class StudentListView(ListView):
    model = Student