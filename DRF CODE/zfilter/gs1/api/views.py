from django.shortcuts import render
from .models import Student
from .serializers import StudentSerliazer
from rest_framework.generics import ListAPIView

# Create your views here.

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerliazer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)