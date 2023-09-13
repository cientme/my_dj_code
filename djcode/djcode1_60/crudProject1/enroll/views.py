from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import StudentRegistration

# Create your views here.


# This Fucnctuin Add New Items And Show All Items.
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            data = User(name=nm , email=em, password=pwd)
            data.save()
            return HttpResponseRedirect('/')
    else:
        form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':form, 'stud':stud})


# This function will update/edit of Student information.
def edit_data(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        data = User.objects.get(pk=id)
    form = StudentRegistration(instance=data)
    return render(request, 'enroll/updatestudent.html', {'form':form})


# This function will delete.
def delete_data(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/')

