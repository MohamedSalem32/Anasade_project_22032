# Generated by Django 4.2.8 on 2023-12-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansade_app', '0006_rename_nom_pointdevente_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointdevente',
            name='gps_lat',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='pointdevente',
            name='gps_long',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]
