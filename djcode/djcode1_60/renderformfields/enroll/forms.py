from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(initial='naufil', help_text="you can type here only 30 char only")
