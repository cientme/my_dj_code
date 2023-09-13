from turtle import width
from django import forms

class StudentRegistration(forms.Form):
    # name = forms.CharField(min_length=3, max_length=30, strip=False)
    # name = forms.CharField(empty_value='naufil')
    name = forms.CharField(error_messages={'required': 'Enter Your Name Please.'})
    roll = forms.IntegerField(error_messages={'required': 'Please Enter A Number.'}, min_value=5, max_value=100)
    price = forms.DecimalField(error_messages={'required': 'Please Enter A Number.'}, min_value=1, max_value=100, max_digits=5, decimal_places=2) # len(max_value) + len(decimal_places) =< len(max_digits)
    rate = forms.FloatField(min_value=5, max_value=100)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=50)
    website = forms.URLField(min_length=5, max_length=50)
    password = forms.CharField(min_length=5, max_length=50, widget=forms.PasswordInput())
    description = forms.CharField(widget=forms.Textarea())
    feedback = forms.CharField(min_length=5, max_length=100, widget=forms.TextInput(attrs={'class': 'somecss1 somecss2', 'id':'uniqueid'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 50}))
    agree = forms.BooleanField(label='I Agree', label_suffix='', error_messages={'required': 'If you are Agree please Check The Box'})

        
