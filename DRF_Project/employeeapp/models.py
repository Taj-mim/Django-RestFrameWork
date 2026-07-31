from django.db import models

# Create your models here.
class employee(models.Model):
    id =models.AutoField(primary_key=True)
    emp_name=models.CharField(max_length=255)
    emp_dept=models.CharField(max_length=255)
    emp_designation=models.CharField(max_length=255)
def __str__(self):
    return self.name
