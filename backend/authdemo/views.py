from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics,viewsets
from rest_framework.exceptions import AuthenticationFailed

import jwt,datetime

from .models import User
from .serializers import LoginSerializer,UserSerializer
# Create your views here.


def LoginFormView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            refresh = RefreshToken.for_user(user)
            token={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            login(request, user)
            return HttpResponse(token)
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    return render(request, 'logout.html', {})

class LoginView(generics.CreateAPIView):
    serializer_class=LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Perform authentication logic here (e.g., login)
            username=serializer.data['username']
            password=serializer.data['password']
            user=authenticate(username=username,password=password)
            
            refresh = RefreshToken.for_user(user)
            data=  {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            return Response({'message': 'Login successful','data':data})
        return Response(serializer.errors, status=400)
    
# class UserView(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class LoginAuthenticationView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        
        user=User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed(' Incorrect Password')
        
        payload={
            'id':user.id,
            'exp':datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.now()
        }
        
        token=jwt.encode(payload,'secret',algorithm='HS256')
        
        response=Response()
        
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt':token,
            'status':status.HTTP_202_ACCEPTED
            }
        
        return response
    
    
    
    