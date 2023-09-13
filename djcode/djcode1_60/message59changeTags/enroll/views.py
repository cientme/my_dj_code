from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistrations
from enroll.models import User
from django.contrib import messages

# Create your views here.

def regi(request):
    messages.info(request, 'Now you can login!!!')
    messages.success(request, 'Profile has been updated!!!')
    messages.warning(request, 'This is warning!!!')
    messages.error(request, 'This is error!!!')
    form = StudentRegistrations()
    return render(request, 'enroll/useregistration.html', {'form': form})
