# Generated by Django 3.1.5 on 2021-03-26 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Emp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='departmentId',
            new_name='DepartmentId',
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='departmentName',
            new_name='DepartmentName',
        ),
    ]
