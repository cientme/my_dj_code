from nturl2path import url2pathname
from django.urls import path
from landing.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index')
]
