from django.shortcuts import render
from enroll.forms import UserRegistration
from enroll.models import User
# Create your views here.

def showformdata(request):
    # if request.method == 'POST': # For save data
    #     form = UserRegistration(request.POST) 
    #     if form.is_valid():
    #         nm = form.cleaned_data['name']
    #         em = form.cleaned_data['email']
    #         pwd = form.cleaned_data['password']
    #         data = User(name=nm, email=em, password=pwd)
    #         data.save()

    if request.method == 'POST': # For update data
        pi = User.objects.get(pk=3)
        form = UserRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            
          
    else:
        form = UserRegistration()
        print('GET data!')
    return render(request, 'enroll/userregistration.html', {'form': form})