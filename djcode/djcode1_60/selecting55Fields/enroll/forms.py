from django import forms
from .models import User

# Create your forms here.

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'email', 'password']
        # fields = '__all__'
        exclude = ['name']

        labels = {
            'name': 'Enter Your Name',
            'email': 'Enter Your Email',
            'password': 'Enter Your Password',
        }

        widgets = {
            'password': forms.PasswordInput()
        }