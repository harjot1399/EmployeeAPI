from rest_framework import serializers
from .models import Employee


class EmployeeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'years_with_company', 'department', 'salary']


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'job_title', 'years_with_company', 'department', 'salary']


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

