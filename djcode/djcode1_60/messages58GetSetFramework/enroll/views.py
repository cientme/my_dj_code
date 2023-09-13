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
            messages.info(request, 'Now you can login!')
            print(messages.get_level(request))
            messages.debug(request, 'this is debug !!!')
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'This is new debug!!')
            print(messages.get_level(request))
        return HttpResponseRedirect('/')
    else:
        form = StudentRegistrations()
    return render(request, 'enroll/useregistration.html', {'form': form})
