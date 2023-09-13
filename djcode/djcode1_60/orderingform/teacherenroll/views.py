from django.shortcuts import render
from teacherenroll.models import Teacher
from . import forms

# Create your views here.

def teacherdata(request):
    teacher = Teacher.objects.all()
    context = {'teacher': teacher}
    return render(request, 'teacherenroll/teacherdata.html', context) 


def teacherform(request):
    tForm = forms.TeacherForm(auto_id=False)
    context = {'tForm': tForm}
    return render(request, 'teacherenroll/teacherform.html', context)