from rest_framework import generics,mixins  
from .models import teacher
from .serializers import teacherserializers
from django.shortcuts import get_object_or_404
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

#Generic views are used to reduce the code and make it more readable and easy to understand
"""
class teacherDetails(generics.ListCreateAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherserializers 
class teacherList(generics.RetrieveUpdateDestroyAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherserializers
    lookup_field='pk'
 """
#viewsets are used to reduce the code and make it more readable and easy to understand

"""
from rest_framework import viewsets
from rest_framework.response import Response
class teacherViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=teacher.objects.all()
        serializer=teacherserializers(queryset,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer=teacherserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def retrieve(self,request,pk=None):
        Teacher = get_object_or_404(teacher, pk=pk)
        serializer = teacherserializers(Teacher)
        return Response(serializer.data)
    def update(self,request,pk=None):
        try:
            teacher_obj=teacher.objects.get(pk=pk)
            serializer=teacherserializers(teacher_obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=404)
    def destroy(self,request,pk=None):
        try:
            teacher_obj=teacher.objects.get(pk=pk)
            teacher_obj.delete()
            return Response({'message': 'Teacher deleted successfully'})
        except teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=404)
    def partial_update(self,request,pk=None):
        try:
            teacher_obj=teacher.objects.get(pk=pk)
            serializer=teacherserializers(teacher_obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=404) """
#modelViewSet is used to provide the functionality of the class based views to the viewsets
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import teacherFilter
class teacherViewSet(viewsets.ModelViewSet):
    queryset=teacher.objects.all()
    serializer_class=teacherserializers
    #filter_backends=[DjangoFilterBackend] this used for default filter backend
    filterset_class=teacherFilter
    filter_backends=[OrderingFilter,SearchFilter,DjangoFilterBackend    ] #this used for search filter backend
  #  fileterset_fields=['teacher_dept'] #this used for filter backend specific filed
    search_fields=['teacher_name'] #search backend specific filed

    ordering_fields=['id'] #order id ascending and descending order