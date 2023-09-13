from django.shortcuts import render

# Create your Views here.

# This View function set cookie.
def setTestCookie(request):
    request.session.set_test_cookie()
    return render(request, 'student/setTestCookie.html')


# This View function check cookie.
def checkTestCookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'student/checkTestCookie.html')


# This View function delete cookie.
def delTestCookie(request):
    request.session.delete_test_cookie()
    return render(request, 'student/delTestCookie.html')

