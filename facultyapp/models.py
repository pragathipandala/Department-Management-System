from django.db import models
from adminapp.models import *

# Create your models here.

class Attendence_Management(models.Model):
    Attendence_ID = models.AutoField(primary_key=True)
    Student_Name = models.TextField(max_length=100)
    Student_Roll = models.TextField(max_length=100)
    Stu_Sem = models.TextField(max_length=100)
    Stu_Branch = models.TextField(max_length=100)
    Att_Date = models.DateField(null = True)
    Att_Subject = models.TextField(max_length=20, null=True)
    Att_Status = models.BooleanField(default = True, null=True)
    Student_Status = models.TextField(default='present', null=True)
    Student_Foregin = models.ForeignKey(Student_Management, on_delete = models.CASCADE, null = True) 
    
    class Meta:
        db_table = 'attendance_management'

class Assignment_details(models.Model):
    Assignment_ID = models.AutoField(primary_key=True)
    Assignment_Name = models.TextField(max_length=100)
    Assignment_Branch = models.TextField(max_length=100, null = True)
    Assignment_Sem = models.TextField(max_length=100, null = True)

    class Meta:
        db_table = "assignment_model"