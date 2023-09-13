import email
from django.shortcuts import render
from userform.models import User
from userform.forms import UserFormRegistration

# Create your views here.

def registerdata(request):
    if request.method == 'POST':
        form = UserFormRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            data = User(name=nm, email=em, password=pwd)
            # data = User(id=1, name=nm, email=em, password=pwd)
            data.save()
            # data = User(id=1)
            # data.delete()
    else:
        form = UserFormRegistration()
    return render(request, 'userform/userdata.html', {'form': form})