from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    correo = models.EmailField(
        max_length=150, unique=True)
    nombre = models.CharField(
        max_length=50)
    apellido = models.CharField(
        max_length=50)
    telefono = models.CharField(
        max_length=10)
    USERNAME_FIELD = 'correo'
    NOMBRE_FIELD = 'nombre'
    APELLIDO_FIELD = 'apellido'
    TELEFONO_FIELD = 'telefono'
    REQUIRED_FIELDS = ['username', 'password']

class Usuario(models.Model):
    id_Usuario = models.AutoField(primary_key=True)    
    apellidoUsuario = models.CharField(max_length=60, blank=False)
    nombreUsuario = models.CharField(max_length=100, blank=False)
    emailUsuario = models.EmailField(blank=False)
    password = models.CharField(max_length=10, blank=False)
    telefonoUsuario = models.CharField(max_length=10, blank=True)
    roles = [
        ("Em", "Emprendedor"),
        ("Cl", "Cliente")
    ]
    rolUsuario = models.CharField(max_length=80, choices=roles)
    class Meta:
        db_table = "Usuario"
        verbose_name = "Usuario registrado"
        verbose_name_plural = "Usuarios"
    def __unicode__(self):
        return self.nombreUsuario
    def __str__(self):
        return self.nombreUsuario

class Emprendedor(models.Model):
    id_Emprendedor = models.AutoField(primary_key=True)
    nombreEmprendimiento = models.CharField(max_length=100, blank=False, default="--")
    descripcionEmp = models.TextField(max_length=1000, blank=False)
    direccion = models.CharField(max_length=50, blank=True)
    redSocialEmp = models.URLField(null=True, blank=True)
    usuario_id = models.ForeignKey(Usuario, to_field="id_Usuario", on_delete=models.CASCADE)
    class Meta:
        db_table = "Emprendedor"
        verbose_name = "Emprendedor registrado"
        verbose_name_plural = "Emprendedores"
    def __unicode__(self):
        return self.nombreEmprendimiento
    def __str__(self):
        return self.nombreEmprendimiento

class Cliente(models.Model):
    id_Cliente = models.AutoField(primary_key=True)
    alias = models.CharField(max_length=100, blank=False, default="--")
    direccion = models.CharField(max_length=50, blank=True)
    usuario_id = models.ForeignKey(Usuario, to_field="id_Usuario", on_delete=models.CASCADE)
    class Meta:
        db_table = "Cliente"
        verbose_name = "Cliente registrado"
        verbose_name_plural = "Clientes"
    def __unicode__(self):
        return self.alias
    def __str__(self):
        return self.alias
"""
class Pedido(models.Model):
    id_Pedido = models.AutoField(primary_key=True)
    fechaPedido = models.DateTimeField()
    fechaEntrega = models.DateTimeField()
    direccion = models.CharField(max_length=50)
    total = models.PositiveIntegerField(blank=False) 
"""
class Categoria(models.Model):
    id_Categoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100, blank=False)
    descripcionCategoria = models.TextField(max_length=1000, blank=False)
    class Meta:
        db_table="Categoria"
        verbose_name = "Categoria de productos"
        verbose_name_plural = "Categorias"
    def __unicode__(self):
        return self.nombreCategoria
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codigodeBarras = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100, blank=False)
    descripcionProducto = models.TextField(max_length=1000, blank=False)
    imagenProducto = models.ImageField(default='Image_Default.jpeg')
    precioUnitario = models.PositiveIntegerField(blank=False) 
    cantidadProducto = models.IntegerField(blank=False, default=0)
    # emprendedor_id = models.ForeignKey(Emprendedor, to_field="id_Emprendedor", on_delete=models.CASCADE)
    id_Categoria = models.ForeignKey(Categoria, to_field="id_Categoria", on_delete=models.CASCADE)
    class Meta:
        db_table = "Producto"
        verbose_name = "Producto de Turnow"
        verbose_name_plural = "Productos"
    def __unicode__(self):
        return self.nombreProducto
    def __str__(self):
        return self.nombreProducto
"""
class Rol(models.Model):
    nombreRol = models.CharField(max_length=15)
    tipoRol = models.IntegerField(default=0)
"""
class CarritoCompras(models.Model):
        producto_nombre = models.CharField(max_length=200)
        producto_precio = models.DecimalField(max_length=10, blank=False, decimal_places=2, max_digits=10)
        producto_cantidad = models.PositiveIntegerField()
        pagos= [
        ("Pagado", "Pagado"),
        ("Pendiente", "Pendiente"),
        ("Rechazado", "Rechazado"),
    ]
        pago = models.CharField(max_length=80, choices=pagos, default="Pendiente")

        producto = models.ManyToManyField(
        Producto,
        related_name= "carrito_producto"
    )
        def __unicode__(self):
            return self.fecha_Hora
        def __str__(self):
            return str(self.pk)
        class Meta:
            db_table = 'carrito'
            verbose_name = 'Carrito'
            verbose_name_plural = 'Carritos'