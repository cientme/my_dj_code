from dataclasses import fields
from logging import PlaceHolder
from tkinter import Widget
from django import forms
from school.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myclass'}),
            'email': forms.TextInput(attrs={'class': 'myclass'}),
            'password': forms.PasswordInput(attrs={'class': 'myclass'}),
          }