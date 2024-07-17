import datetime
import jwt

from django.conf import settings

from rest_framework import parsers, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.shortcuts import render,get_object_or_404
from rest_framework import generics,mixins,status,authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser

from .forms import BlogForm,ImageForm,LoginForm
from .models import Blog,BlogImages,Statistics
from .serializers import BlogSerializer,BlogImagesSerializer,StatSerializer
# Create your views here.

@api_view(['POST', 'GET'])
@permission_classes([])
def formapi(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return Response({"message": "Form saved"}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:  # GET request
        form = BlogForm()   
        context = {
            'form': form
        }
        return render(request, "form1.html", context)
    
@api_view(['POST', 'GET'])
@permission_classes([])
def formimageapi(request):
    if request.method == 'POST':
        form2=ImageForm(request.POST,request.FILES)
        if form2.is_valid():
            form2.save()
            return Response({"message": "Form saved"}, status=status.HTTP_201_CREATED)
        return Response(form2.errors, status=status.HTTP_400_BAD_REQUEST)
    else:  # GET request
        form2=ImageForm()
        context = {
            'form2':form2
        }
        return render(request, "form2.html", context)
    
@api_view(['PUT','POST','GET','PATCH'])
@permission_classes([])
def formupdateapi(request,pk=None):
    obj=get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return Response({"message": "Form saved"}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:  # GET request
        form = BlogForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, "form1.html", context)
    
class Blogcreateview(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    parser_class = [MultiPartParser, FormParser]
    serializer_class = BlogSerializer
    
class BlogImagesCreateView(generics.CreateAPIView):
    queryset=BlogImages.objects.all()
    serializer_class=BlogImagesSerializer

class BlogMixinView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    
class BlogRetrieveUpdateDestroyMixinView(mixins.UpdateModelMixin,
                                        mixins.RetrieveModelMixin,
                                        mixins.DestroyModelMixin,
                                        generics.GenericAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    authentication_classes=[authentication.TokenAuthentication]
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    
    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)
    
    
@api_view(['GET','PUT','DELETE'])
def ImageUpdateDeleteView(request,parent_id=None,id=None):
    try:
        obj = BlogImages.objects.get(blog__id=parent_id, id=id)
    except BlogImages.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'PUT':
        serializer = BlogImagesSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=204) 
    elif request.method == 'GET':
        serializer = BlogImagesSerializer(obj)
        return Response(serializer.data)

class StatsView(generics.ListCreateAPIView):
    queryset=Statistics.objects.all()
    serializer_class=StatSerializer