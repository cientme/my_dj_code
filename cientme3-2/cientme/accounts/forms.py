from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate
from accounts.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=225,  widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')
        
    
class AccountAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))   

    class Meta:
        model = Account
        fields = ('username', 'password')

    
    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid Login")
                

class UserPasswordChangeForm(PasswordChangeForm):
    # oldpass = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old Password'}))
    # newpass = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}))
    # newpassconfirm = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm New Password'}))

    class Meta:
        model = Account
        fields = ('oldpass', 'newpass', 'newpassconfirm')


class UserSetPasswordForm(SetPasswordForm):
    class Meta:
        model = Account
        fields = ('username','password')