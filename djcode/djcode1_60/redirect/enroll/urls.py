from django.urls import path
from enroll import views

urlpatterns = [
    path('userform', views.showformdata, name='userform'),
    path('success/', views.success, name='success'),
]
