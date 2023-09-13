from django.contrib import admin
from school.models import Student

# Register your models here.

@admin.register(Student)
class StudentModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'course')