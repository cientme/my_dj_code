from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
# Create your views here.

def home(request):
    print('I am View')
    return HttpResponse('This is Home Page')

def excp(request):
    print('I am except View')
    a = 10/0
    return HttpResponse('This is Except Page')


def user_info(request):
    print("I Am User Info View.")
    context = {'name': 'Naufil'}
    return TemplateResponse(request, 'blog/user.html',context)