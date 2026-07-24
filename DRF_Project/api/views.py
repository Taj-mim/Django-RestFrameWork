from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentdoc(request):
    details={
        'id' : 1,
        'name' :'fatema',
        'roll' :12,
    }
    return JsonResponse(details)