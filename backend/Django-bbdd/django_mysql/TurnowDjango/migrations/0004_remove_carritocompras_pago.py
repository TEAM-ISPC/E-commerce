# Generated by Django 4.1.2 on 2023-06-19 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TurnowDjango', '0003_alter_carritocompras_options_carritocompras_pago_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritocompras',
            name='pago',
        ),
    ]