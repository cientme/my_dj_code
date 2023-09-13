from django import forms
from .models import User


# Create your forms here.

class StudentRegistrations(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        } 