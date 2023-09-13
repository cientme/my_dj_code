from django.shortcuts import render
from school.models import Student, Teacher, Contractor

# Create your views here.

def home(request):
    students_data = Student.objects.all()
    teacher_data = Teacher.objects.all()
    contractor_data = Contractor.objects.all()
    return render(request, 'school/home.html', {'students': students_data, 'teachers': teacher_data, 'contractors': contractor_data})