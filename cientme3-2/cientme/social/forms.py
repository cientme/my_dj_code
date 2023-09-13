from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    caption = forms.CharField(
    label='', 
    widget=forms.Textarea(attrs={
        'rows':6, 
        'class':'form-control', 
        'placeholder':"What's in Your mind..."
        }))

    class Meta:
        model = Post
        fields = ('caption',)

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={
            # 'class':'form-control', 
            'placeholder':"Comment here..."
            }))

    class Meta:
        model = Comment
        fields = ('comment',)
