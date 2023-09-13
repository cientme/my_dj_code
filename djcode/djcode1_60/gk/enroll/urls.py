from django.urls import path
from enroll import views

urlpatterns = [
    path('userform', views.userRegistration, name='userform'),
]
