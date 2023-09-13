from django.shortcuts import render
from enroll.forms import UserRegistration
# Create your views here.

def success(request):
    return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method == 'POST': 
        form = UserRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            print(nm)
            print(em)
            print(pwd)
            
          
    else:
        form = UserRegistration()
        print('GET data!')
    return render(request, 'enroll/userregistration.html', {'form': form})