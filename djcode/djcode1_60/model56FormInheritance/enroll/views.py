from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration, Techerregitration

# Create your views here.

def studentform(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    else:
        form = StudentRegistration()
    return render(request, 'enroll/student.html', {'form': form})


def teacherform(request):
    if request.method == 'POST':
        form = Techerregitration(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/teacher/')
    else:
        form = Techerregitration()
    return render(request, 'enroll/teacher.html', {'form': form})

