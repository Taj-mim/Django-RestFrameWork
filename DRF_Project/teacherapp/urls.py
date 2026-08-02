from django.urls import path ,include
#from .views import teacherDetails
#from .views import teacherList
from .views import teacherViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('teacher',teacherViewSet,basename='teacher')

urlpatterns = [
   # path('teacher/',teacherDetails.as_view()),
   # path('teacher/<int:pk>/',teacherList.as_view()),
    path('',include(router.urls))
]
