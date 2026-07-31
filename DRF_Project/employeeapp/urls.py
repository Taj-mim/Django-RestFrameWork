from django.urls import path
from .views import EmployeeDetails

urlpatterns = [
    path('employee/',EmployeeDetails.as_view())
]
