# Generated by Django 3.1.4 on 2020-12-03 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_pelicula_fecha_estreno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='director',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='pelicula',
            old_name='duracion',
            new_name='paginas',
        ),
    ]
