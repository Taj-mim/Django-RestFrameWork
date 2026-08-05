from .views import RegisterView,LoginView,ProfileView,LogoutView
from rest_framework import urlpatterns
from django.urls import path

urlpatterns = [

    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('protected/',ProfileView.as_view(),name="Profile"),
    path('logout/',LogoutView.as_view(),name="logout")
    
]
