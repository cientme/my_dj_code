from audioop import avg
from django.shortcuts import render
from school.models import Student
from datetime import date, time
from django.db.models import Avg, Sum, Min, Max, Count

# Create your views here.

def home(request):
    # student_data = Student.objects.all().aggregate(Avg('marks'))
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    totale = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    totalecount = student_data.aggregate(Count('marks'))

    print(average)
    print('Return', student_data)
    print()

    context =  {
        'students': student_data, 
        'average': average, 
        'totale': totale,
        'minimum': minimum,
        'maximum': maximum,
        'totalecount': totalecount, 
        }
    # print('SQL Query', student_data.query)
    return render(request, 'school/home.html', context)