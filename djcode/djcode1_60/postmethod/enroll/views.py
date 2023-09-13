from django.shortcuts import render
from enroll.models import Student 
from enroll.forms import StudentRegistration
# Create your views here.

def studentinfo(request):
    stud = Student.objects.all()
    print('myoutput', stud)
    context = {'stud': stud}
    return render(request, 'enroll/studetail.html', context)

def showformdata(request):
    form = StudentRegistration()
    return render(request, 'enroll/userregistraion.html', {'form': form})