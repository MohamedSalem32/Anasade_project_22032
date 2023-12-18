

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Produit, FamilleProduit

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'liste_produits.html', {'produits': produits})

def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    return render(request, 'detail_produit.html', {'produit': produit})
