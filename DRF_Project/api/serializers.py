from rest_framework import serializers
from Student_app.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta :
        model=Student
        fields= "__all__"
