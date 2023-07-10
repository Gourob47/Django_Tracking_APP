from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#Here First table is for Employee Registration as One-Many Relationship
class Employee(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    employee_name=models.CharField(max_length=100)

    def __str__(self):
        return self.employee_name

# Monitor table uses for  Device use History and Employee use history.
class Monitor(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    accessories_id=models.CharField(max_length=100)
    employee_name=models.CharField(max_length=100)
    checkout_Time=models.CharField(max_length=100)
    return_Time=models.CharField(max_length=100)


    def __str__(self):
        return self.accessories_id