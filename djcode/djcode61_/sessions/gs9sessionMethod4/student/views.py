from email.policy import default
import re
from django.shortcuts import render

# Create your Views here.
 
def setSession(request):
    request.session['name'] = 'Hemi'
    return render(request, 'student/setSession.html')


def getSession(request):
    name = request.session.get('name')
    return render(request, 'student/getSession.html', {'name': name,})

 
def delSession(request):
    request.session.flush()
    request.session.clear_expired() # this method clear data brom db.
    return render(request, 'student/delSession.html')
