# Generated by Django 5.0.1 on 2024-01-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansade_app', '0009_alter_panier_date_ajout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panier',
            name='code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='panier',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='panier',
            name='label',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='panier_produit',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pointdevente',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='produit',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]