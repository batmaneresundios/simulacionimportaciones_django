# Generated by Django 4.2.4 on 2023-10-16 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importacionesChina', '0009_alter_resultado_iva_alter_resultado_tasa_aduana_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='costo_envio',
            field=models.IntegerField(),
        ),
    ]