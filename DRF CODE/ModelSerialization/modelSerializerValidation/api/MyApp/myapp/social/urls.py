from django.urls import path
from social import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
