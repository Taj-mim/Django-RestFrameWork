from django.urls import path, include
from .views import FileUpload 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'upload', FileUpload, basename='upload')

urlpatterns = [
    path('', include(router.urls)),
]
