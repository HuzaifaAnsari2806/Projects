from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=200)
    published_date=models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title