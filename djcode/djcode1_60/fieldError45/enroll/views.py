from django.shortcuts import render
from enroll.models import Student 
from enroll.forms import StudentRegistration
# Create your views here.

def success(request):
    return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method == 'POST': 
        form = StudentRegistration(request.POST)
        if form.is_valid():
            print('Form Validated')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('Name:', name)
            print('Email:', email)
            print('Password:', password)
            
          
    else:
        form = StudentRegistration()
        print('GET data!')
    return render(request, 'enroll/userregistration.html', {'form': form})