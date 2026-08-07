#this is for DRF
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import RegisterSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate , login,logout
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#Register API view for user registration
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#login view
class LoginView(APIView):
    serializer=LoginSerializer
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")

        user =authenticate(
            username=username,
            password= password
        )

        if user is not None:
            login(request,user)
            return Response(request.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Protected logout
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({

            "username": request.user.username,

            "email": request.user.email

        })

#logout view

class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        logout(request)
        return Response({
            "message":"Logged Out"
        })
        """
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
# Create your views here.

#Register API view for user registration
class RegisterView(APIView):

    def get(self, request):

        form = RegisterForm()

        return render(
            request,
            "accounts/register.html",
            {
                "form": form
            }
        )

    def post(self, request):

        form = RegisterForm(request.POST)

        if form.is_valid():

            User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )

            return redirect("login")

        return render(
            request,
            "accounts/register.html",
            {
                "form": form
            }
        )
#login view
class LoginView(APIView):

    def get(self, request):

        form = LoginForm()

        return render(
            request,
            "accounts/login.html",
            {
                "form": form
            }
        )

    def post(self, request):

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect("profile")

        return render(
            request,
            "accounts/login.html",
            {
                "form": form
            }
        )

#Protected logout
from rest_framework.permissions import IsAuthenticated


class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return render(
            request,
            "accounts/login.html",
        )

#logout view
class LogoutView(APIView):

    def get(self, request):

        logout(request)

        return redirect("login")