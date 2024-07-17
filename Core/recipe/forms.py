from django import forms
from .models import Recipe,RecipeIngredient,RecipeIngredientImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields=['name','desc','directions']
        
class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model=RecipeIngredient
        fields=['name','quantity','unit']
        
class RecipeIngredientImageForm(forms.ModelForm):
    class Meta:
        model=RecipeIngredientImage
        fields=['image']