from django import forms
from django.core import validators

def start_with_s(value):
    if value[0] != 'n':
        raise forms.ValidationError("Name should be start with latter 'n' ")


class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[start_with_s])
    email = forms.EmailField()