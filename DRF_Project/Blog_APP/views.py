from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from .paginations import CustomTeacherPagination 

# Create your views here.
class BlogDetails(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomTeacherPagination  # Use the custom pagination class for this view
class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
class BlogList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'
