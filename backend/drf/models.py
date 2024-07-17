import pathlib
import uuid
from django.db import models

# Create your models here.

def image_upload_handler(instance,filename):
    fpath=pathlib.Path(filename)
    new_filename=str(uuid.uuid1())
    return f'images/{new_filename}{fpath.suffix}'

class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    
    def __str__(self):
        return self.title
    
    
    
class BlogImages(models.Model):
    blog=models.ForeignKey(Blog,related_name='images',on_delete=models.CASCADE,default=Blog)
    images=models.ImageField(upload_to=image_upload_handler,blank=True,null=True)
    
    def __str__(self):
        return self.blog.title
    

class Statistics(models.Model):
    field_name=models.CharField(max_length=100)
    value=models.IntegerField()
    
    def __str__(self):
        return self.field_name
    
    