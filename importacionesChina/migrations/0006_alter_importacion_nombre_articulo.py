# Generated by Django 4.2.4 on 2023-10-14 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importacionesChina', '0005_alter_importacion_nombre_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importacion',
            name='nombre_articulo',
            field=models.CharField(max_length=100),
        ),
    ]
