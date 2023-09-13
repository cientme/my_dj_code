from django.shortcuts import render
from .models import Student
from .serializers import StudentSerliazer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerliazer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city']
    filterset_fields = ['name','city']