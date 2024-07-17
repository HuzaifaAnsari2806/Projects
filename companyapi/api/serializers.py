from rest_framework import serializers

from .models import Company,Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    employees=serializers.SerializerMethodField()
    class Meta:
        model=Company
        fields="__all__"
        
    def get_employees(self, obj):
        # Assuming you want to retrieve employees related to this company
        queryset = Employee.objects.filter(company=obj)
        # Serialize the queryset of employees using a serializer if needed
        employee_serializer = EmployeeSerializer(queryset, many=True, context=self.context)
        return employee_serializer.data
    
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"