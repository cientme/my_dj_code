from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View

# Create your views here.

# class HomeTemplateView(TemplateView):
#     template_name = 'school/home.html'

class HomeTemplateView(TemplateView):
    template_name = 'school/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Hemi'
        context['roll'] = 101
        # context = {'name': 'Hemi', 'roll': 101}
        print(context)
        print(kwargs)
        return context


