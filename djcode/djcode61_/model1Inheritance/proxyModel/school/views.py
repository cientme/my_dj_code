from django.shortcuts import render
from .models import ExamCenter, MyExamCenter

# Create your views here.

def home(request):
    exam_center = ExamCenter.objects.all()
    my_exam_center = MyExamCenter.objects.all()
    return render(request, 'school/home.html', {'examcenters': exam_center, 'myexamcenters': my_exam_center})