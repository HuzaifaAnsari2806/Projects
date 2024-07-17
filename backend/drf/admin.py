from django.contrib import admin

from .models import Blog,BlogImages
# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogImages)