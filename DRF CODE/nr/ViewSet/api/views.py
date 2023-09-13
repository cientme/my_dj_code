from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class StudentApi(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
        

    def retrieve(self, request, pk=None):
        if id is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)


    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created!!!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated!!!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated Partially!!!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg': 'Data Deleted!!!'})

 
            
