from django.contrib import admin
from .models import Recipe,RecipeIngredient,RecipeIngredientImage
# Register your models here.

class RecipeIngredientInline(admin.StackedInline):
    model=RecipeIngredient
    extra=0
    readonly_fields=['quantity_as_float','as_mks','as_imperial']
    

class RecipeAdmin(admin.ModelAdmin):
    inlines=[RecipeIngredientInline]
    list_display=['id','name','timestamp','active']
    search_fields=['name']
    readonly_fields=['timestamp','updated']
    raw_id_fields=['user']
    
# admin.site.register(RecipeIngredient)
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(RecipeIngredientImage)