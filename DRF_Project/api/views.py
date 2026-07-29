#from django.shortcuts import render
#from django.http import JsonResponse
from Student_app.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def studentdoc(request):
    if request.method == 'GET':
        #get all the student details
        details=Student.objects.all()
        serializer=StudentSerializer(details,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif(request.method=='POST'):
        #Fill up the form
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def studentdetails(request,pk):
    try:
        student=Student.objects.get(pk=pk) #here get method ask for single value
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method== 'GET'):
         serializer=StudentSerializer(student)
         return Response(serializer.data,status=status.HTTP_200_OK)
    #for updating data
    elif request.method == 'PUT':
        serializer=StudentSerializer(student,data=request.data) #data=request.data is used to accept value,to be more specific we use student to know about the specific id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    #deleting data
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)