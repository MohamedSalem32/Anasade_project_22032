# Generated by Django 4.2.8 on 2023-12-24 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansade_app', '0002_alter_familleproduit_nom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prix',
            old_name='date_effet',
            new_name='date_validite',
        ),
        migrations.RenameField(
            model_name='prix',
            old_name='valeur',
            new_name='montant',
        ),
        migrations.AddField(
            model_name='panier',
            name='description',
            field=models.CharField(default='Aucune description', max_length=255),
        ),
        migrations.AddField(
            model_name='panier',
            name='nom',
            field=models.CharField(default='Nom par défaut', max_length=255),
        ),
        migrations.AddField(
            model_name='pointdevente',
            name='adresse',
            field=models.TextField(default='Adresse par défaut'),
        ),
        migrations.AddField(
            model_name='pointdevente',
            name='nom',
            field=models.CharField(default='Adresse par défaut', max_length=100),
        ),
        migrations.AddField(
            model_name='ponderation',
            name='nom',
            field=models.CharField(default='Adresse par défaut', max_length=100),
        ),
    ]
