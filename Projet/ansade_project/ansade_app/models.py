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
    quantite = models.PositiveIntegerField()
    date_creation = models.DateField(auto_now_add=True)
    famille = models.ForeignKey(FamilleProduit, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('produit_detail', args=[str(self.id)])
    
# Enfin, définir les autres classes
class Panier(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed
    nom = models.CharField(max_length=255, default='Nom par défaut')
    description = models.CharField(max_length=255, default='Aucune description')

    def __str__(self):
        return f"Panier {self.id},{self.nom}"
    
    def get_absolute_url(self):
        return reverse('panier_detail', args=[str(self.id)])


class Prix(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='prix_set')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_validite = models.DateField()
    def __str__(self):
         return f"{self.montant} - {self.produit}"

    def get_absolute_url(self):
        return reverse('prix_detail', args=[str(self.id)])
    


class Ponderation(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    valeur = models.DecimalField(max_digits=5, decimal_places=2)
    # Add other fields as needed
    nom = models.CharField(max_length=100,default='Adresse par défaut')
    def __str__(self):
        return f"Ponderation {self.id},{self.nom}"
    
    
    def get_absolute_url(self):
        return reverse('ponderation_detail', args=[str(self.id)])



class PointDeVente(models.Model):
    wilaya = models.CharField(max_length=255)
    moughataa = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    gps = models.CharField(max_length=255)
    # Add other fields as needed
    nom = models.CharField(max_length=100,default='Adresse par défaut')
    adresse = models.TextField(default='Adresse par défaut')  # Ajoutez une valeur par défaut ici

    def __str__(self):
        return f"{self.village}, {self.moughataa}, {self.wilaya}, {self.nom}"

    def get_absolute_url(self):
        return reverse('pointdevente_detail', args=[str(self.id)])
    