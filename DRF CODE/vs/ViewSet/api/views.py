from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print('***************List**************')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Detail', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print('***************Retrieve**************')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Detail', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def post(self, request):
        print('***************Create**************')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Detail', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg', 'Data Created!!!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def update(self, request, pk):
        print('***************Update**************')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Detail', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        print('***************Partial Update*************')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Detail', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated partially!!!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        print('***************Delete**************')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Detail', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted!!!'})