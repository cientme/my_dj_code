from curses import keyname
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    modile = forms.IntegerField()
    key = forms.CharField(widget=forms.HiddenInput())
