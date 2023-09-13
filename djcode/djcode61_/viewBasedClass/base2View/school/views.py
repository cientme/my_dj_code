from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
# Create your views here.

def homefun(request):
    return render(request, 'school/home.html')

class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html')

####################################################################


def aboutfun(request):
    context = {'msg': 'Welcome To GeekyShows Function Based View'}
    return render(request, 'school/about.html', context)

class AboutClassView(View):
    def get(self, request):
        context = {'msg': 'Welcome To GeekyShows Function Based View'}
        return render(request, 'school/about.html', context)

def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submited!')
    else:
        form = ContactForm()
        return render(request, 'school/contact.html', {'form': form})


class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submited!')
    


########################################################################

# def newsfun(request):
#     context = {'info': 'CBI enquiry Why GeekyShows Earns Less Money'}
#     return render(request,'school/news.html' , context)

# def newsfun(request):
#     template_name = 'school/news.html'
#     context = {'info': 'CBI enquiry Why GeekyShows Earns Less Money'}
#     return render(request, template_name, context)

def newsfun(request, template_name):
    template_name = template_name
    context = {'info': 'CBI enquiry Why GeekyShows Earns Less Money'}
    return render(request, template_name, context)


class NewsClassView(View):
    # template_name = 'school/news.html'
    template_name = ''
    def get(self, request):
        context = {'info': 'CBI enquiry Why GeekyShows Earns Less Money'}
        return render(request, self.template_name, context)