from django.contrib import admin
 

 # ansade_app/admin.py
from django.contrib import admin
from .models import FamilleProduit, Produit, PointDeVente, Prix, Panier, Panier_Produit

admin.site.register(FamilleProduit)
admin.site.register(Produit)
admin.site.register(PointDeVente)
admin.site.register(Prix)
admin.site.register(Panier)
admin.site.register(Panier_Produit)

# Register your models here.
