from django import forms
from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"
    def clean(self):
        data = self.cleaned_data
        name=data.get('name')
        qs=User.objects.all().filter(name__icontains=name)
        if qs.exists():
            self.add_error("name", f"{name} , already exists.")
        
        return data
    
class UserFormOld(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=20)
    password=forms.CharField(max_length=10)
    
class UserCreationForm(ModelForm):
     class Meta:
        model=User
        fields="__all__"
