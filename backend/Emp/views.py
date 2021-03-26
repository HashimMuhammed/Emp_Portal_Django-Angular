from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse 
from .models import Employees,Departments
from .serializers import DepartmentSerializer,EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def departmentApi(request,id=0):
    if (request.method=='GET'):
        departments=Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif(request.method=='POST'):
        departmentsdata=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=departmentsdata)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("failed",safe=False)
    elif(request.method=='PUT'):
        departmentsdata=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=departmentsdata['DepartmentId'])
        print(department)
        departments_serializer=DepartmentSerializer(department,data=departmentsdata)
        
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("failed",safe=False)
    elif(request.method=='DELETE'):
        departmentsdata=JSONParser().parse(request)
        departmentdata=Departments.objects.get(DepartmentId=departmentsdata['DepartmentId'])
        departmentdata.delete()
        return JsonResponse("Failed Successfully",safe=False)
@csrf_exempt   
def employeeApi(request,id=0):
    if (request.method=='GET'):
        employees=Employees.objects.all()
        employee_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    elif (request.method=='POST'):
        employeesdata=JSONParser().parse(request)
        employee_serializer=EmployeeSerializer(data=employeesdata)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed",safe=False)
    elif request.method=='PUT':
        employeesdata=JSONParser().parse(request)
        employees=Employees.objects.get(EmployeeId=employeesdata['EmployeeId'])
        employee_serializer=EmployeeSerializer(employees,data=employeesdata)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed",safe=False)
    elif (request.method=='DELETE'):
        employees_data=JSONParser().parse(request)
        employeesdata=Employees.objects.get(EmployeeId=employees_data['EmployeeId'])
        employeesdata.delete()
        return JsonResponse("Successfully Deleted",safe=False)

@csrf_exempt
def SaveFile(request):
    return


            

