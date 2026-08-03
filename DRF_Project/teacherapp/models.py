from django.db import models

# Create your models here.
class teacher(models.Model):
    id =models.AutoField(primary_key=True)
    teacher_id=models.CharField(max_length=255,unique=True,null=True,blank=True)
    teacher_name=models.CharField(max_length=255)
    teacher_dept=models.CharField(max_length=255)
    teacher_designation=models.CharField(max_length=255)
    def __str__(self):
        return self.teacher_name

