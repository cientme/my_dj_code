from urllib.request import Request
from django import forms

class StudentRegistration(forms.Form):
    # name = forms.CharField(label='Your Name', label_suffix=':', initial='Naufil', required=False, disabled=True)
    # email = forms.EmailField(label='Your Email', label_suffix=':', initial='rjanaufil@gmail.com', required=False, disabled=True)
    # Phone = forms.IntegerField(label='Phone Number', label_suffix=':', initial=8920162537, required=False, disabled=True)
    # gender = forms.CharField(label='Male/Female', label_suffix=':', initial='Male', required=False, disabled=True)
    # hindden = forms.CharField(widget=forms.HiddenInput())

    name = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 4 :
            raise forms.ValidationError('Enter more than or equale to 4 char.')
        if len(valemail) < 10 :
            raise forms.ValidationError('Enter more than or equale to 10 char.')