from rest_framework import status
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from employeeapp.models import employee
from rest_framework.decorators import APIView
from .models import employee

# Create your views here.
#class based view which include CRUD
class EmployeeDetails(APIView):
    def get(self,request):
        details=employee.objects.all()
        serializer=EmployeeSerializer(details,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
            serializer=EmployeeSerializer(employee,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
            serializer=EmployeeSerializer(data=request.data)
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)