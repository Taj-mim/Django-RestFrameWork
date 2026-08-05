from rest_framework import serializers
from .models import uploadfiles

class uploadfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model=uploadfiles
        fields='__all__'