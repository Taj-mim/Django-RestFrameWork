from rest_framework import generics,mixins  
from .models import teacher
from .serializers import teacherserializers
# Create your views here.
#mixxins are used to add the functionality of the class based views to the generic views
"""
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
"""
class teacherDetails(generics.ListCreateAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherserializers 
class teacherList(generics.RetrieveUpdateDestroyAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherserializers
    lookup_field='pk'