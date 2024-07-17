from typing import Iterable, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.text import slugify
from django.db.models import Q
from django.conf import settings

author=settings.AUTH_USER_MODEL

class UserQuerySet(models.QuerySet):
    def search(self,query=None):
        if not query:
            return self.none()
        lookups=Q(name__icontains=query) | Q(email__icontains=query)
        return self.filter(lookups)


class UserManager(models.Manager):
    def get_queryset(self):
        return UserQuerySet(self.model,using=self._db)
    
    def search(self,query):
        return self.get_queryset().search(query=query)


# Create your models here.
class User(models.Model):
    auth=models.ForeignKey(author,blank=True,null=True,on_delete=models.SET_NULL)
    name=models.CharField(max_length=100)
    slug=models.SlugField(null=True,blank=True)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=10)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    # date_of_birth=models.DateField(auto_now=False,auto_now_add=False,default=timezone.now)
    
    objects=UserManager()
    
    def get_absolute_url(self):
        return f'/base/{self.slug}/'
    
    def save(self):
        if self.slug is None:
            self.slug=slugify(self.name)
        return super().save()