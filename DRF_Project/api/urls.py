from django.urls import path
from . import views

urlpatterns = [
    #Api endpoint
    path('students/',views.studentdoc),

]
