from django.shortcuts import render
from school.models import Student
# Create your views here.

def home(request):
    # students = Student.objects.get(pk=1)
    # students = Student.objects.first()
    # students = Student.objects.order_by('name').first()

    # students = Student.objects.last()
    # students = Student.objects.latest('pass_date')

    # students = Student.objects.earliest('pass_date')
    # students = Student.objects.all()
    # print(students.exists())
    # one_data = Student.objects.get(pk=1)
    # print(students.filter(pk=one_data.pk).exists())

    # students = Student.objects.create(name='Sameer', roll=112, city='bakaro', marks=80, pass_date='2015-06-26')

    # students, created = Student.objects.get_or_create(name='Anisha', roll=113, city='bakaro', marks=70, pass_date='2015-06-26')
    # print(created)

    # students = Student.objects.get(pk=12).update(name='kabir', marks=50) 
    # students = Student.objects.filter(pk=12).update(name='kabir', marks=50)
    # students = Student.objects.filter(marks=50).update(city='Passing')

    # students, created = Student.objects.update_or_create(pk=12, name="kabir", defaults={'name': 'kohli'})
    # print(created)

    # objs = [
    #     Student(name='manmeet', roll=114, city='koriyo', marks=45, pass_date='2019-06-18'),
    #     Student(name='azhar', roll=115, city='aligarh', marks=75, pass_date='2020-04-28'),
    #     Student(name='Rihana', roll=116, city='Firozabaad', marks=65, pass_date='2017-07-14'),
    # ]
    # students = Student.objects.bulk_create(objs)

    # all_students = Student.objects.all()
    # for stu in all_students:
    #     stu.city = 'canmoro'
    # students = Student.objects.bulk_update(all_students, ['city'])

    # students = Student.objects.in_bulk([1, 2])
    # print(students[2].name)
    # students = Student.objects.in_bulk([])
    # students = Student.objects.in_bulk()

    # students = Student.objects.filter(marks=50).delete()
    # students = Student.objects.all().delete()

    # students = Student.objects.all()
    # print(students.count())

    students = Student.objects.all().explain()
    print(students)
    print('Return:', students)
    return render(request, 'school/home.html', {'student': students})