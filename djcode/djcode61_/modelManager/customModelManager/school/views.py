from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    # student_data = Student.objects.all()
    student_data = Student.students.all()
    print('Student Data', student_data)
    print()
    print('Return Query', student_data.query)
    return render(request, 'school/home.html', {'students': student_data})