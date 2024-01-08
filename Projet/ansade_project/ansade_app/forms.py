# ansade_app/forms.py
from django import forms
from .models import *
from tempus_dominus.widgets import DatePicker

class FamilleProduitForm(forms.ModelForm):
    class Meta:
        model = FamilleProduit
        fields = ['nom', 'description']  # Ajoutez les champs de votre modèle ici

    
class PanierForm(forms.ModelForm):
    class Meta:
        model = Panier
        fields = ['date_ajout', 'description', 'label', 'code']
        widgets = {
            'date_ajout': forms.DateInput(attrs={'type': 'date'}),
        }
class PrixForm(forms.ModelForm):
    class Meta:
        model = Prix
        fields = ['montant','produit','point_vente','date_validite']

class Panier_ProduitForm(forms.ModelForm):
    class Meta:
        model = Panier_Produit
        fields = ['nom','ponderation','prix','quantite','code']

class PointDeVenteForm(forms.ModelForm):
    class Meta:
        model = PointDeVente
        fields = ['wilaya','moughataa','commune','gps_lat','gps_long','code']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'famille', 'code', 'date_creation']

 
