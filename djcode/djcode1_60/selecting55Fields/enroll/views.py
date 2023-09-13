from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import StudentRegistration


# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            data = User(name=nm, email=em, password=pwd)
            data.save()
        return HttpResponseRedirect('/')
    else:
        form = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': form})