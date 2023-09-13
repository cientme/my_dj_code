from django.urls import path
from teacherenroll import views

urlpatterns = [
    path('teacherdata/', views.teacherdata, name='teacherdata'),
    path('teacherform/', views.teacherform, name='teacherform'),
]
