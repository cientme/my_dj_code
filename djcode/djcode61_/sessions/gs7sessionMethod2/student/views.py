from email.policy import default
import re
from django.shortcuts import render

# Create your Views here.
 
def setSession(request):
    request.session['name'] = 'Hemi'
    # request.session.set_expiry(20)          # set expiry time
    request.session.set_expiry(0)           # set expire at bowser close
    return render(request, 'student/setSession.html')


def getSession(request):
    name = request.session.get('name')
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request, 'student/getSession.html', {'name': name,})

 
def delSession(request):
    request.session.flush()
    request.session.clear_expired() # this method clear data brom db.
    return render(request, 'student/delSession.html')
