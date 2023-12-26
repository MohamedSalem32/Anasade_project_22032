 # ansade_app/models.py
from django.db import models
from django.urls import reverse

# Create your models here.


 

 
# Définir d'abord FamilleProduit
class FamilleProduit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.nom
    
    def get_absolute_url(self):
        return reverse('familleproduit_detail', args=[str(self.id)])

# Ensuite, définir Produit avec une référence à FamilleProduit
class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateField()
    famille = models.ForeignKey(FamilleProduit, on_delete=models.CASCADE)
    # Add other fields as needed
    code = models.CharField(max_length=50, unique=True,default='le code du produit par défaut' )  # Ajout de la colonne 'code'

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('produit_detail', args=[str(self.id)])

class PointDeVente(models.Model):
    wilaya = models.CharField(max_length=255)
    moughataa = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    gps_lat = models.DecimalField(max_digits=9, decimal_places=6)
    gps_long = models.DecimalField(max_digits=9, decimal_places=6)
# Add other fields as needed
    code = models.CharField(max_length=100,default='Nom par défaut')
 
    def __str__(self):
        return f"{self.commune}, {self.moughataa}, {self.wilaya}, {self.code}"

    def get_absolute_url(self):
        return reverse('pointdevente_detail', args=[str(self.id)])
    


class Prix(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='prix_set')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_validite = models.DateField()
    point_vente = models.ForeignKey(PointDeVente, on_delete=models.CASCADE,null=True,blank=True )
    
    def __str__(self):
         return f"{self.montant} - {self.produit}"
    
    def get_absolute_url(self):
        return reverse('prix_detail', args=[str(self.id)])
 
class Panier(models.Model):
   
    date_ajout = models.DateTimeField()
    description = models.CharField(max_length=255, default='Aucune description')
    code = models.CharField(max_length=50, unique=True, default='le code du panier par défaut')
    label = models.CharField(max_length=100, default='Label par défaut')
    
     
    def __str__(self):
        return f"Panier {self.id},{self.code}"
    
    def get_absolute_url(self):
        return reverse('panier_detail', args=[str(self.id)])


class Panier_Produit(models.Model):
    code =  models.ForeignKey(Panier, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix = models.ForeignKey(Prix, on_delete=models.CASCADE)
    ponderation = models.DecimalField(max_digits=5, decimal_places=2)
    # Add other fields as needed
    nom = models.CharField(max_length=100,default='Adresse par défaut')
    
    def __str__(self):
        return f"Panier_Produit {self.id},{self.nom}"
    
    
    def get_absolute_url(self):
        return reverse('ponderation_detail', args=[str(self.id)])


# Enfin, définir les autres classes


    





