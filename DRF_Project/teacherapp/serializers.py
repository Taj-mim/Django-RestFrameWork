from rest_framework import serializers
from teacherapp.models import teacher

class teacherserializers(serializers.ModelSerializer):
    class Meta :
        model=teacher
        fields="__all__"