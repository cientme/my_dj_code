from email.policy import default
import re
from django.shortcuts import render

# Create your Views here.

def setSession(request):
    request.session['name'] = 'Hemi'
    request.session['lname'] = 'Bora'
    return render(request, 'student/setSession.html')


def getSession(request):
    name = request.session.get('name')
    keys = request.session.keys()
    items = request.session.items()
    # age = request.session.setdefault('age', 26)
    return render(request, 'student/getSession.html', {'name': name, 'keys': keys, 'items': items})

 
def delSession(request):
    request.session.flush()
    return render(request, 'student/delSession.html')
