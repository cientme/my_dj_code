from email.mime import message
from django import forms
from django.core import validators
from enroll.models import User

# Create your fome here.

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {
            'name': 'Enter Name', 
            'email': 'Enter Email', 
            'password': 'Enter Password'
            }
        

        widgets = {
            'password': forms.PasswordInput(),
            }
