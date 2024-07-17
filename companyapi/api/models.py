import pathlib
import uuid
from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('Smartphones','Smartphones')))
    timestamp=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
def image_upload_handler(instance,filename):
    fpath=pathlib.Path(filename)
    new_filename=str(uuid.uuid1())
    return f'images/{new_filename}{fpath.suffix}'
    

class Employee(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    position=models.CharField(max_length=50,choices=(('Manager','Manager'),('Software Developer','SD'),('Team Leader','TL')))
    joinig_date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to=image_upload_handler,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    