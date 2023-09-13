from django import forms
from .models import User
# Create your form here.

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name':'Enter Your Name', 'email':'Enter Your Email', 'password':'Enter Your Password'}
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
                
            'email': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'class': 'form-control'}),
        }
