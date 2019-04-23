# Generated by Django 2.2 on 2019-04-21 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrarUsuarios',
            fields=[
                ('Rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('PrimerNombre', models.CharField(blank=True, max_length=200, null=True)),
                ('PrimerApellido', models.CharField(blank=True, max_length=200, null=True)),
                ('Direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('Correo', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
