from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import generics,viewsets,status
from rest_framework.decorators import action,api_view,permission_classes
from faker import Faker

from .serializers import CompanySerializer,EmployeeSerializer
from .models import Company,Employee
from .forms import EmployeeForm
# Create your views here.

@api_view(['POST', 'GET'])
@permission_classes([])
def formapi(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save()
            image_name = instance.image.name.split('/')[-1]
            return Response({"message": "Form saved",'image-name':image_name}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:  # GET request
        form = EmployeeForm()
        context = {
            'form': form
        }
        return render(request, "form1.html", context)
        
        
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    @action(detail=True,methods=['get'])
    def emp(self,request,pk=None):
        company=Company.objects.get(pk=pk)
        emps=Employee.objects.filter(company=company)
        emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request })
        return Response(emps_serializer.data)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "count": queryset.count(), 
            "Companies": serializer.data
        })
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "count": queryset.count(),  
            "Employees": serializer.data
        })