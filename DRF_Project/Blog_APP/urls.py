from django.urls import path
from .views import BlogDetails, BlogList, CommentDetails
urlpatterns = [
    path('blog/',BlogDetails.as_view()),
    path('blog/<int:pk>/',BlogList.as_view()),
    path('comment/<int:pk>/',CommentDetails.as_view())
]