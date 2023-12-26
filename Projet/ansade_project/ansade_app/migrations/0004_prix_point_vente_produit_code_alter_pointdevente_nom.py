# Generated by Django 4.2.8 on 2023-12-25 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ansade_app', '0003_rename_date_effet_prix_date_validite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prix',
            name='point_vente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ansade_app.pointdevente'),
        ),
        migrations.AddField(
            model_name='produit',
            name='code',
            field=models.CharField(default='le code du produit par défaut', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='pointdevente',
            name='nom',
            field=models.CharField(default='Nom par défaut', max_length=100),
        ),
    ]
