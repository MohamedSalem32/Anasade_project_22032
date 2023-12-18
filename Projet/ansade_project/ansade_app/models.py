from django.db import models

# Create your models here.


class FamilleProduit(models.Model):
    nom = models.CharField(max_length=255)

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    famille = models.ForeignKey(FamilleProduit, on_delete=models.CASCADE)
     
