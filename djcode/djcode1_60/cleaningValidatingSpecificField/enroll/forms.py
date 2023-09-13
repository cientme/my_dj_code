from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    # def clean_name(self):
    #     valname = self.changed_data[1]
    #     if len(valname) < 4:
    #         raise forms.ValidationError('Enter more than  equale 4 char.')
    #     return valname