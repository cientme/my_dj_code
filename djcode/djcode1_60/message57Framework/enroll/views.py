from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistrations
from enroll.models import User
from django.contrib import messages

# Create your views here.

def regi(request):
    if request.method == 'POST':
        form = StudentRegistrations(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your account has been create successfully!!!')
            messages.info(request, 'Now you can login!')
        return HttpResponseRedirect('/')
    else:
        form = StudentRegistrations()
    return render(request, 'enroll/useregistration.html', {'form': form})
