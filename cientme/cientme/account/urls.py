from urllib.parse import urlparse
from django.urls import path
from account.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
