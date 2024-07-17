from django.contrib import admin
from  .models import *

# Register your models here.

class blogpostAdmin(admin.ModelAdmin):
    list_display =['title']

admin.site.register(BlogPost,blogpostAdmin)