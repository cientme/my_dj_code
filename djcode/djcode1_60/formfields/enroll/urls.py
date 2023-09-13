from django.urls import path
from enroll import views

urlpatterns = [
    path('stu', views.studentinfo, name='stu'),
    path('userform', views.showformdata, name='userform'),
]
