from django.urls import path
from . import views

urlpatterns = [
    #Api endpoint
    path('students/',views.studentdoc),
    #anothe api endpoint 
    path('students/<int:pk>/',views.studentdetails),

]
