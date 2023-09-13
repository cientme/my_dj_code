from email.policy import default
from django.shortcuts import render

# Create your Views here.

def setSession(request):
    request.session['name'] = 'Hemi'
    request.session['lname'] = 'Bora'
    return render(request, 'student/setSession.html')


def getSession(request):
    # name = request.session['name']
    name = request.session.get('name')
    lname = request.session.get('lname')
    return render(request, 'student/getSession.html', {'name': name, 'lname': lname})

 
def delSession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delSession.html')
