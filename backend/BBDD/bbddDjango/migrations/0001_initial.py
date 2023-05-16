# Generated by Django 4.2.1 on 2023-05-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emprendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionEmp', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('redSocialEmp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaPedido', models.DateField()),
                ('fechaEntrega', models.DateField()),
                ('direccion', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=30)),
                ('descripcionProducto', models.CharField(max_length=100)),
                ('precioUnitario', models.IntegerField()),
                ('categoriaProducto', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidoUsuario', models.CharField(max_length=30)),
                ('nombreUsuario', models.CharField(max_length=30)),
                ('emailUsuario', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('telefonoUsuario', models.CharField(max_length=7)),
            ],
        ),
    ]
