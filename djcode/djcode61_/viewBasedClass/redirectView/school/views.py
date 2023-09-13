from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.

class YouTubeRedirectView(RedirectView):
    url = 'http://www.youtube.com'

# class YouRedirectView(RedirectView):
#     url = '/'

class YouRedirectView(RedirectView):
    pattern_name = 'minindex'
    permanent = True
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['pk'] = 100 
        return super().get_redirect_url(*args, **kwargs)