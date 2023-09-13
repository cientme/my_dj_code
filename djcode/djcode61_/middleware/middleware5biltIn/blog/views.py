from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    print("I am View")
    return HttpResponse("<h1>This Is Home Page</h1>")