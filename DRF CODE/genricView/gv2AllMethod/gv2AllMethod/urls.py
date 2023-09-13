
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.LCStudentApi.as_view(), name='stuapi'),
    path('studentapi/<int:pk>/', views.RUDStudentApi.as_view(), name='stuapiId'),
  
]