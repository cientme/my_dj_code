from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# cleare your forms here.

class SignUpform(UserCreationForm):
    password2 = forms.CharField(label='confirm password (again)', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'email': 'Email'
        }

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login',]
        labels = {
            'email': 'Email'
        }

class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'email': 'Email'
        }