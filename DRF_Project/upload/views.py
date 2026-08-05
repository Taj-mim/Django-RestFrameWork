from rest_framework import viewsets as ViewSets
from rest_framework.response import Response
from .serializers import uploadfilesSerializer
from .models import uploadfiles 


# Create your views here.
class FileUpload(ViewSets.ModelViewSet):
    queryset = uploadfiles.objects.all()
    serializer_class = uploadfilesSerializer
    