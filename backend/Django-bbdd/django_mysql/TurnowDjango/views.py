from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from .models import Categoria, Producto, CustomUser
from .serializers import ProductoSerializer
from .serializers import CategoriaSerializer
import mercadopago
import json

class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        correo = request.data.get('correo', None)
        password = request.data.get('password', None)
        user = authenticate(correo=correo, password=password)
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

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        
class ListarUsuarios(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response(serializer.data)

class verProductos(generics.ListCreateAPIView):
    permission_classes = [AllowAny] 
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class verProductoDetalle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny] 
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class verCategorias(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class verCategoriaDetalle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class agregarProducto(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProcessPaymentAPIView(APIView):
    def post(self, request):
        try:
            request_values = json.loads(request.body)
            payment_data = {
                "transaction_amount": float(request_values["transaction_amount"]),
                "token": request_values["token"],
                "installments": int(request_values["installments"]),
                "payment_method_id": request_values["payment_method_id"],
                "issuer_id": request_values["issuer_id"],
                "payer": {
                    "email": request_values["payer"]["email"],
                    "identification": {
                        "type": request_values["payer"]["identification"]["type"],
                        "number": request_values["payer"]["identification"]["number"],
                    },
                },
            }

            sdk = mercadopago.SDK("")

            payment_response = sdk.payment().create(payment_data)

            payment = payment_response["response"]
            status = {
                "id": payment["id"],
                "status": payment["status"],
                "status_detail": payment["status_detail"],
            }

            return Response(data={"body": status, "statusCode": payment_response["status"]}, status=201)
        except Exception as e:
            return Response(data={"body": payment_response}, status=400)
        
class retornarPagado(APIView):  
    def get(self, request):
        return Response({"respuesta": "aprobado"})

class customjsonybajarstock(APIView):
    permission_classes = [IsAdminUser] 
    def patch(self, request, pk, cantidad):
        model = get_object_or_404(Producto, pk=pk) #
        data = {"cantidadProducto": model.cantidadProducto - int(cantidad)}
        serializer = ProductoSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save() 
            agregarcustomjson={"respuesta": "aprobado"}
            agregarcustomjson.update(serializer.data) 
            return Response(agregarcustomjson)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)