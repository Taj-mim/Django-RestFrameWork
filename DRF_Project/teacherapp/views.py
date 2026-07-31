from rest_framework import generics,mixins  
from .models import teacher
from .serializers import teacherserializers
# Create your views here.
class teacherDetails(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherserializers
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class teacherList(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherserializers
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.delete(request,pk)