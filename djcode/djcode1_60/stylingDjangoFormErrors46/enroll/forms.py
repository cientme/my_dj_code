from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    name = forms.CharField(error_messages={'required': 'Enter Your Name.'})
    email = forms.EmailField(error_messages={'required': 'Enter Your Email.'}, min_length=5, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required': 'Enter Your Password.'}, min_length=5, max_length=50)