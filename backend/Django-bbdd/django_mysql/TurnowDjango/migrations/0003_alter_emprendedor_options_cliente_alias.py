# Generated by Django 4.2.1 on 2023-05-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TurnowDjango', '0002_emprendedor_nombreemprendimiento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprendedor',
            options={'verbose_name': 'Emprendedor registrado', 'verbose_name_plural': 'Emprendedores'},
        ),
        migrations.AddField(
            model_name='cliente',
            name='alias',
            field=models.CharField(default='--', max_length=100),
        ),
    ]
