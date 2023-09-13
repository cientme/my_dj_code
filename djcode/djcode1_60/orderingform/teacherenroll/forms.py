from django import forms

class TeacherForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    teaching_exp = forms.CharField()
    bio_data = forms.CharField()