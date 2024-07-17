from django import forms

from .models import Blog,BlogImages

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields="__all__"
        
class ImageForm(forms.ModelForm):
    class Meta:
        model=BlogImages
        fields="__all__"
        
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=10)