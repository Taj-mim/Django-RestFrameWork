from django.urls import path
from .views import teacherDetails
from .views import teacherList

urlpatterns = [
    path('teacher/',teacherDetails.as_view()),
    path('teacher/<int:pk>/',teacherList.as_view())
]
