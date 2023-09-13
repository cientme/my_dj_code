from django.shortcuts import render
from school.models import Student, Teacher
from django.db.models import Q
# Create your views here.

def home(request):
    # students = Student.objects.all()

    # students = Student.objects.filter(marks=75)

    # students = Student.objects.exclude(marks=75) 
    
    # students = Student.objects.order_by('marks') # for ascending order.
    # students = Student.objects.order_by('-marks') # for descending.
    # students = Student.objects.order_by('?') # for random order.
    # students = Student.objects.order_by('id')[:5]
    # students = Student.objects.order_by('id').reverse()[:5]

    # students = Student.objects.values() # It give All data in the form of dictionarty.
    # students = Student.objects.values('name', 'city') It Gives specifuc data in the form of tuple.
    
    # students = Student.objects.values('name', 'city') # It give All data in dictionarty.

    # students = Student.objects.values_list(named=True) # It give All data in tuple.
    # students = Student.objects.values_list('id', 'name', 'marks', named=True) # It give All data in tuple.

    # students = Student.objects.using('default') # It tells What Database You are using.

    students = Student.objects.dates('pass_date', 'month') # It tells What Database You are using.

#################### Second Table 'Teacher' Started  #####################
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # students = qs2.union(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # students = qs2.union(qs1, all=True) # it Shows all duplicate values

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # students = qs2.intersection(qs1) 

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # students = qs2.difference(qs1) 

    ##################### AND OR operators ########################
    # students = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # students = Student.objects.filter(id=6,  roll=106)
    # students = Student.objects.filter(Q(id=6) & Q(roll=106))

    # students = Student.objects.filter(id=6) | Student.objects.filter(roll=107)
    students = Student.objects.filter(Q(id=6) | Q(roll=107))
    print('Return:', students)
    print()
    print('SQL QuerySet:', students.query)
    return render(request, 'school/home.html', {'students': students})