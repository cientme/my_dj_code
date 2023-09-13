from logging import PlaceHolder
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(
        widget=forms.Textarea(
            attrs= {
            'class': 'classcss1', 
            'cols': 100,
            'rows': 20, 
            }
        ))
