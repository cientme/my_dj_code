
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentApi.as_view(), name='student'),
]
