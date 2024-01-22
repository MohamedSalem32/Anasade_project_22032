 # ansade_app/models.py
from django.db import models
from django.urls import reverse
from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget
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
    code = models.CharField(max_length=50, unique=True)  # Ajout de la colonne 'code'

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
    code = models.CharField(max_length=100)
 
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
    date_ajout = models.DateField()
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    
     
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
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Panier_Produit {self.id},{self.nom}"
    
    
    def get_absolute_url(self):
        return reverse('Panier_Produit_detail', args=[str(self.id)])


# Enfin, définir les autres classes

## les codes des ressources pour l'import/export

class FamilleProduitResource(resources.ModelResource):
    class Meta:
        model = FamilleProduit
        fields = '__all__'

class ProduitResource(resources.ModelResource):
 
    class Meta:
        model = Produit
        fields = '__all__'

class PointDeVenteResource(resources.ModelResource):
    class Meta:
        model = PointDeVente
        fields = '__all__'

class PrixResource(resources.ModelResource):
    class Meta:
        model = Prix
        fields = "__all__"

class PanierResource(resources.ModelResource):
    class Meta:
        model = Panier
        fields = '__all__'

class Panier_ProduitResource(resources.ModelResource):
    
    class Meta:
        model = Panier_Produit
        fields = '__all__'

from django.db.models import Sum

def calculer_indice_prix_annuel(annee):
    # Filtrer les paniers produits pour une année spécifique
    paniers_produits_annuels = Panier_Produit.objects.filter(code__date_ajout__year=annee)

    # Calculer la somme pondérée des prix
    somme_ponderation_prix = paniers_produits_annuels.aggregate(somme=Sum(models.F('ponderation') * models.F('prix__montant')))['somme']

    # Calculer la somme des pondérations
    somme_ponderation = paniers_produits_annuels.aggregate(somme=Sum('ponderation'))['somme']

    # Calculer l'indice des prix annuel
    # Vérifier si les valeurs sont None avant de faire la division
    if somme_ponderation_prix is not None and somme_ponderation is not None and somme_ponderation != 0:
        indice_prix_annuel = somme_ponderation_prix / somme_ponderation
    else:
        indice_prix_annuel = 0
    return indice_prix_annuel


