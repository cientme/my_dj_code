from urllib.parse import urlparse
from django.urls import path
from social import views

urlpatterns = [
    path('', views.home, name='home'),
]
