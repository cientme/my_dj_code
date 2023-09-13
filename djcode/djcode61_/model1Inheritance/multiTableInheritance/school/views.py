from django.shortcuts import render
from school.models import ExamCenter, Student

# Create your views here.

def home(request):
    exam_center = ExamCenter.objects.all()
    student_data = Student.objects.all()
    return render(request, 'school/home.html', {'examcenters': exam_center, 'students': student_data})

    