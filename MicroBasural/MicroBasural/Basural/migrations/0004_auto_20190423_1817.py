# Generated by Django 2.2 on 2019-04-23 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basural', '0003_remove_registrarusuarios_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrarusuarios',
            name='Correo',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='registrarusuarios',
            name='Direccion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='registrarusuarios',
            name='PrimerApellido',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='registrarusuarios',
            name='PrimerNombre',
            field=models.CharField(max_length=200),
        ),
    ]
