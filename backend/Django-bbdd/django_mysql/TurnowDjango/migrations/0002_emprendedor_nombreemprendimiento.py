# Generated by Django 4.2.1 on 2023-05-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TurnowDjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprendedor',
            name='nombreEmprendimiento',
            field=models.CharField(default='--', max_length=100),
        ),
    ]
