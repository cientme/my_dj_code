from django import forms
from django.core import validators
from enroll.models import User

# Create your fome here.

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


