from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    correo = serializers.EmailField(
        required=True)
    nombre = serializers.CharField(
        required=True)
    apellido = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)
    telefono = serializers.CharField(
        max_length=10)



    class Meta:
        model = get_user_model()
        fields = ('correo', 'nombre', 'apellido', 'password', 'telefono')
    def validate_password(self, value):
        return make_password(value)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoCompraSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(max_length=200)
    producto_precio = serializers.FloatField()
    producto_cantidad = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CarritoCompras
        fields = ('__all__')