from django.db import models

class Departments(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=100)

class Employees(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=100)
    Departments=models.CharField(max_length=100)
    Doj=models.DateField(auto_now=False)
    PhotoField=models.CharField(max_length=100)
