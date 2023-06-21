# Generated by Django 4.1.2 on 2023-06-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TurnowDjango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_nombre', models.CharField(max_length=200)),
                ('producto_precio', models.DecimalField(decimal_places=2, max_digits=10, max_length=10)),
                ('producto_cantidad', models.PositiveIntegerField()),
            ],
        ),
    ]
