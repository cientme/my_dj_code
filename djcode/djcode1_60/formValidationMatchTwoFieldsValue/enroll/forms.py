from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    repassword = forms.CharField(label='Password(again)',widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data.get('password')
        valrepwd = self.cleaned_data.get('repassword')
        if valpwd != valrepwd:
            raise forms.ValidationError('passwords do not match.')