from django.contrib import admin

# Register your models here.
from .models import Employees,Departments

admin.site.register(Departments)
admin.site.register(Employees)