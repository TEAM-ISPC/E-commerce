# Generated by Django 4.2.1 on 2023-06-03 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TurnowDjango', '0003_alter_emprendedor_options_cliente_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagenProducto',
            field=models.ImageField(default='Image_Default.jpeg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='redSocialEmp',
            field=models.URLField(blank=True, null=True),
        ),
    ]
