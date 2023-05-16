from django.db import models

# Create your models here.

class Usuario(models.Model):    
    apellidoUsuario = models.CharField(max_length=30)
    nombreUsuario = models.CharField(max_length=30)
    emailUsuario = models.EmailField()
    password = models.CharField(max_length=10)
    telefonoUsuario = models.CharField(max_length=7)

class Emprendedor(models.Model):
    descripcionEmp = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    redSocialEmp = models.CharField(max_length=30)

class Cliente(models.Model):
    direccion = models.CharField(max_length=50)

class Pedido(models.Model):
    fechaPedido = models.DateField()
    fechaEntrega = models.DateField()
    direccion = models.CharField(max_length=50)
    total = models.IntegerField()

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcionProducto = models.CharField(max_length=100)
    #imagenProducto = models.
    precioUnitario = models.IntegerField() 
    categoriaProducto = models.CharField(max_length=15)

