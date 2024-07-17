from django.shortcuts import render
from rest_framework import generics,status,permissions
from rest_framework.response import Response

from .models import BlogPost
from.serializers import BolgPostSerializer

# Create your views here.
class BlogPostCreateView(generics.ListCreateAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BolgPostSerializer
    
    def delete(self,request):
        self.queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BolgPostSerializer
    lookup_field='pk'
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]