from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    modile = forms.IntegerField()
    com = forms.CharField()
