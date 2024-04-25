from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Avg, Count
from .models import Employee
from .serializers import EmployeeRetrieveSerializer, EmployeeDetailSerializer, EmployeeCreateSerializer
from django.shortcuts import get_object_or_404


class EmployeeStatsView(APIView):
    http_method_names = ['get', 'post']

    def get(self, request):
        employees = Employee.objects.all().order_by('-years_with_company')
        total_employees = employees.count()
        average_years_with_company = employees.aggregate(Avg("years_with_company"))
        average_salary = employees.aggregate(Avg("salary"))
        serializer = EmployeeRetrieveSerializer(employees, many=True)

        response_data = {
            "total": total_employees,
            "average_years_with_company": average_years_with_company['years_with_company__avg'],
            "average_salary": average_salary['salary__avg'],
            "employees": serializer.data
        }

        return Response(response_data, status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeCreateSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            response_data = {
                "status": 200,
                "message": "New employee added",
                "id": employee.id
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailsView(APIView):
    http_method_names = ['get', 'put', 'patch', 'delete']

    def get(self, request, user):
        employee = get_object_or_404(Employee, pk=user)
        serialized_employee = EmployeeDetailSerializer(employee)
        return Response(serialized_employee.data, status.HTTP_200_OK)

    def put(self, request, user):
        employee = get_object_or_404(Employee, pk=user)
        serialized_employee = EmployeeDetailSerializer(employee, data=request.data)
        if serialized_employee.is_valid():
            serialized_employee.save()
            response_data = {
                "status": 200,
                "message": "Employee updated"
            }
            return Response(response_data, status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user):
        employee = get_object_or_404(Employee, pk=user)
        serialized_employee = EmployeeDetailSerializer(employee, data=request.data, partial=True)
        if serialized_employee.is_valid():
            serialized_employee.save()
            response_data = {
                "status": 200,
                "message": "Employee modified"
            }
            return Response(response_data, status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user):
        employee = get_object_or_404(Employee, pk=user)
        employee.delete()
        response_data = {
            "status": 200,
            "message": "Employee deleted"
        }
        return Response(response_data, status.HTTP_200_OK)
