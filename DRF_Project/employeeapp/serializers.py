from rest_framework import serializers
from employeeapp.models import employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields="__all__"