from django.shortcuts import render
from django.views import View


# Create your views here.

def home_screen_view(request, *args, **kwargs):
    context = {}
    return render(request, 'personal/home.html', context)
    
