# GenricAPIView and Model MIxin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# List And Create classes - PK is NOT Required.
class LCStudentApi(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
 
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
# Retrieve, Updated and Destroy classes - PK is Required
class RUDStudentApi(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
 
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
 
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

