# Generated by Django 4.2.4 on 2023-10-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importacionesChina', '0002_resultado_remove_importacion_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultado',
            old_name='total_compra',
            new_name='total_compra_clp',
        ),
        migrations.AddField(
            model_name='resultado',
            name='total_compra_usd',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
