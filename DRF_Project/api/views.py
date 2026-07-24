from django.shortcuts import render
from django.http import JsonResponse
from Student_app.models import Student

# Create your views here.
def studentdoc(request):
    
    details=Student.objects.all()
    student_list=list(details.values())
    return JsonResponse(student_list, safe=False)