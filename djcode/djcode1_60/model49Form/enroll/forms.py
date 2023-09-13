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
        error_messages = {
            'name': {'required': 'Name is compulsory'}, 
            'email': {'required':'Email is compulsory'}, 
            'password': {'required':'Password is compulsory'},
            }

        widgets = {
            'password': forms.PasswordInput(),
            'name': forms.TextInput(
                attrs={
                    'class': 'myclass', 
                    'placeholder': 'Enter Your Name',
                    'email': 'Enyer Your email',
                    'password': 'Enyer Your password',
                    }
                ),
            'email': forms.TextInput(
                attrs={
                    'class': 'myclass', 
                    'placeholder': 'Enter Your Emil',
                    
                    }
                ),
            'password': forms.TextInput(
                attrs={
                    'class': 'myclass', 
                    'placeholder': 'Enter Your Password',
                    
                    }
                ),
            }
