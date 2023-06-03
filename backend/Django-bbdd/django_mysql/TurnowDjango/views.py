from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializers import UserSerializer
# from .models import Categoria, Producto, CustomUser
from rest_framework.permissions import AllowAny
# from .serializers import ProductoSerializer
# from .serializers import CategoriaSerializer
# from rest_framework import viewsets


class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return Response(
                status=status.HTTP_200_OK)
        return Response(
            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)