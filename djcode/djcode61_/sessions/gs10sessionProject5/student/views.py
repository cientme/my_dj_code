from django.shortcuts import render, HttpResponse

# Create your Views here.
 
def setSession(request):
    request.session['name'] = 'Hemi'
    return render(request, 'student/setSession.html')


def getSession(request):
    if 'name' in request.session:
        name = request.session.get('name')
        request.session.modified = True
        return render(request, 'student/getSession.html', {'name': name,})
    else:
        return HttpResponse("<h1>Your session has expired...</h1>")

 
def delSession(request):
    request.session.flush()
    request.session.clear_expired() # this method clear data brom db.
    return render(request, 'student/delSession.html')
