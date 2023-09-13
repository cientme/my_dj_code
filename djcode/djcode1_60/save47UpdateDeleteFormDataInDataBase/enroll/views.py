from django.shortcuts import render
from .models import User
from enroll.forms import StudentRegistration
# Create your views here.

def success(request):
    return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method == 'POST': 
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            # data = User(name=nm, email=em, password=pwd) #data Insurt
            # data = User(id=1, name=nm, email=em, password=pwd) # data Update
            # data.save()
            data = User(id=1)
            data.delete()
          
    else:
        form = StudentRegistration()
        print('GET data!')
    return render(request, 'enroll/userregistration.html', {'form': form})