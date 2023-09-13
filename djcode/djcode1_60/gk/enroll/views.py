from django.shortcuts import render
from enroll.models import Student 
from enroll.forms import StudentRegistration
# Create your views here.


# def userRegistration(request):
#     form = StudentRegistration(label_suffix='',initial={'name':'naufil'})
#     return render(request, 'enroll/userregistration.html', {'form':form})

def userRegistration(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print('Form validated')
            print('Name:', name)
            print('Email:', email)

    else:
        form = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':form})