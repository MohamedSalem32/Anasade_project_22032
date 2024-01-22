from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# admin.py

from .models import * 



admin.site.register(FamilleProduit)
admin.site.register(Produit)
admin.site.register(PointDeVente)
admin.site.register(Prix)
admin.site.register(Panier)
admin.site.register(Panier_Produit)

# Register your models here.
# ansade_app/admin.py
 