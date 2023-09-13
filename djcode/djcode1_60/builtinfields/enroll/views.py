from django.shortcuts import render
from django.http import HttpResponseRedirect
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
            roll = form.cleaned_data['roll']
            price = form.cleaned_data['price']
            rate = form.cleaned_data['rate']
            comment = form.cleaned_data['comment']
            email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            password = form.cleaned_data['password']
            description = form.cleaned_data['description']
            feedback = form.cleaned_data['feedback']
            agree = form.cleaned_data['agree']
            print('Name:', name)
            print('Roll:', roll)
            print('Price:', price)
            print('Rate:', rate)
            print('Comment:', comment)
            print('Email:', email)
            print('Website:', website)
            print('Password:', password)
            print('Description:', description)
            print('Feedback:', feedback)
            print('Agree:', agree)
           
    else:
        form = StudentRegistration()
        print('GET data!')
    return render(request, 'enroll/userregistraion.html', {'form': form})