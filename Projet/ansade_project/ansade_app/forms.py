# ansade_app/forms.py
from django import forms
from .models import *

class FamilleProduitForm(forms.ModelForm):
    class Meta:
        model = FamilleProduit
        fields = ['nom', 'description']  # Ajoutez les champs de votre modèle ici

class PanierForm(forms.ModelForm):
    class Meta:
        model = Panier
        fields = ['nom', 'description']
    
class PrixForm(forms.ModelForm):
    class Meta:
        model = Prix
        fields = ['montant']

class PonderationForm(forms.ModelForm):
    class Meta:
        model = Ponderation
        fields = ['valeur']

class PointDeVenteForm(forms.ModelForm):
    class Meta:
        model = PointDeVente
        fields = ['nom', 'adresse']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix']