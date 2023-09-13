from email.policy import default
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def setcookie(request):
    ''' Where response is a variable we can give any name '''
    response = render(request, 'student/setCookie.html')
    # response.set_cookie('name', 'Hemi', max_age=60)
    response.set_signed_cookie('name', 'Hemi', salt='nm', expires=datetime.utcnow()+timedelta(days=2))
    return response


def getcookie(request):
    name = request.get_signed_cookie('name', default='Guest', salt='nm')
    return render(request, 'student/getCookie.html', {'name': name})

def delcookie(request):
    response = render(request, 'student/delCookie.html')
    response.delete_cookie('name')
    return response