from django.shortcuts import render
from enroll.forms import SignUpform
from django.contrib import messages

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!')
        form = SignUpform()
    else:
        form = SignUpform()
    return render(request, 'enroll/singup.html', {'form': form})