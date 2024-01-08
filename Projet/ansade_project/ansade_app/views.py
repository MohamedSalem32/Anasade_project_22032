# ansade_app/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import loader
from .models import Produit, FamilleProduit, Panier, Prix, Panier_Produit, PointDeVente
from django.views import View
from django.views.generic.edit import CreateView
from .forms import *
from import_export import resources
from tablib import Dataset
from .models import ProduitResource 

# Classe de ressource pour l'import/export des Produits
class ProduitResource(resources.ModelResource):
    class Meta:
        model = Produit

# Fonction pour l'export des produits au format CSV
def export_produits_csv(request):
    produit_resource = ProduitResource()
    dataset = produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="produits.csv"'
    return response 
# Fonction pour l'importation des produits à partir d'un fichier CSV
def import_produits_csv(request):
    if request.method == 'POST':
        produit_resource = ProduitResource()
        dataset = Dataset()

        new_produits = request.FILES['myfile']

        if not new_produits.name.endswith('csv'):
            messages.error(request, 'Le fichier doit être au format CSV')
            return render(request, 'ansade_app/import_data.html')

        imported_data = dataset.load(new_produits.read().decode('latin-1'), format='csv')
        result = produit_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            produit_resource.import_data(dataset, dry_run=False)  # Actually import now
            messages.success(request, 'Les données ont été importées avec succès.')
        else:
            messages.error(request, 'Il y a des erreurs dans votre fichier.')

    return render(request, 'ansade_app/import_data.html')         
# Classe de vue pour afficher la liste des produits
class ProduitListView(ListView):
    model = Produit
    template_name = 'ansade_app/produit_list.html'

    
 

# Classe de vue pour afficher les détails d'un produit spécifique
class ProduitDetailView(DetailView):
    model = Produit
    template_name = 'ansade_app/produit_detail.html'

class ProduitCreateView(CreateView):
    model = Produit
    template_name = 'ansade_app/produit_form.html'
    fields = ['nom', 'description', 'famille','prix','date_creation','code']


class ProduitUpdateView(UpdateView):
    model = Produit
    template_name = 'ansade_app/produit_form.html'
    fields = ['nom', 'description', 'famille','prix','date_creation', 'code']

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'ansade_app/produit_confirm_delete.html'
    success_url = reverse_lazy('produit_list')

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produits')
    else:
        form = ProduitForm()

    return render(request, 'ajouter_produit.html', {'form': form})

# Classe de vue pour afficher la liste des familles de produits

# Classe de ressource pour l'import/export des Familles de Produits
class FamilleProduitResource(resources.ModelResource):
    class Meta:
        model = FamilleProduit

# Fonction pour l'export des familles de produits au format CSV
def export_famillesproduits_csv(request):
        familleproduit_resource = FamilleProduitResource()
        dataset = familleproduit_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="famillesproduits.csv"'
        return response      
class FamilleProduitListView(ListView):
    model = FamilleProduit
    template_name = 'ansade_app/familleproduit_list.html'

 

# Classe de vue pour afficher les détails d'une famille de produit spécifique
class FamilleProduitDetailView(DetailView):
    model = FamilleProduit
    template_name = 'ansade_app/familleproduit_detail.html'


class FamilleProduitListView(ListView):
    model = FamilleProduit
    template_name = 'ansade_app/familleproduit_list.html'

class FamilleProduitCreateView(CreateView):
    model = FamilleProduit
    template_name = 'ansade_app/familleproduit_form.html'
    fields = ['nom', 'description']

class FamilleProduitUpdateView(UpdateView):
    model = FamilleProduit
    template_name = 'ansade_app/familleproduit_form.html'
    fields = ['nom', 'description']

class FamilleProduitDeleteView(DeleteView):
    model = FamilleProduit
    template_name = 'ansade_app/familleproduit_confirm_delete.html'
    success_url = reverse_lazy('familleproduit_list')

# Classe de vue pour afficher la liste des paniers
    
# Classe de ressource pour l'import/export des Paniers
class PanierResource(resources.ModelResource):
    class Meta:
        model = Panier
# Fonction pour l'export des paniers au format CSV
def export_paniers_csv(request):
    panier_resource = PanierResource()
    dataset = panier_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="paniers.csv"'
    return response
class PanierListView(ListView):
    model = Panier
    template_name = 'ansade_app/panier_list.html'

    

# Classe de vue pour afficher les détails d'un panier spécifique


class PanierDetailView(DetailView):
    model = Panier
    template_name = 'ansade_app/panier_detail.html'

class PanierCreateView(CreateView):
    model = Panier
    template_name = 'ansade_app/panier_form.html'
    fields = ['date_ajout', 'description','label','code']


class PanierUpdateView(UpdateView):
    model = Panier
    template_name = 'ansade_app/panier_form.html'
    fields = ['date_ajout', 'description','label','code']


class PanierDeleteView(DeleteView):
    model = Panier
    template_name = 'ansade_app/panier_confirm_delete.html'
    success_url = reverse_lazy('panier_list') 

   

# Classe de vue pour afficher la liste des prix
    
# Classe de ressource pour l'import/export des Prix
class PrixResource(resources.ModelResource):
    class Meta:
        model = Prix
# Fonction pour l'export des prix au format CSV
def export_prix_csv(request):
    prix_resource = PrixResource()
    dataset = prix_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prix.csv"'
    return response 
class PrixListView(ListView):
    model = Prix
    template_name = 'ansade_app/prix_list.html'

       

# Classe de vue pour afficher les détails d'un prix spécifique
class PrixDetailView(DetailView):
    model = Prix
    template_name = 'ansade_app/prix_detail.html'

class PrixCreateView(CreateView):
    model = Prix
    template_name = 'ansade_app/prix_form.html'
    fields = ['montant','produit','point_vente','date_validite']

class PrixUpdateView(UpdateView):
    model = Prix
    template_name = 'ansade_app/prix_form.html'
    fields = ['montant','produit','point_vente','date_validite']


class PrixDeleteView(DeleteView):
    model = Prix
    template_name = 'ansade_app/prix_confirm_delete.html'
    success_url = reverse_lazy('prix_list')

# Classe de ressource pour l'import/export des Paniers_Produits
class Panier_ProduitResource(resources.ModelResource):
    class Meta:
        model = Panier_Produit
# Fonction pour l'export des paniers produits au format CSV
def export_paniersproduits_csv(request):
    panier_produit_resource = Panier_ProduitResource()
    dataset = panier_produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="paniersproduits.csv"'
    return response
# Classe de vue pour afficher la liste des pondérations
class Panier_ProduitListView(ListView):
    model = Panier_Produit
    template_name = 'ansade_app/Panier_Produit_list.html'

     

# Classe de vue pour afficher les détails d'une pondération spécifique
class Panier_ProduitDetailView(DetailView):
    model = Panier_Produit
    template_name = 'ansade_app/Panier_Produit_detail.html'

class Panier_ProduitCreateView(CreateView):
    model = Panier_Produit
    template_name = 'ansade_app/Panier_Produit_form.html'
    fields = ['nom','ponderation','prix','quantite','code']


class Panier_ProduitUpdateView(UpdateView):
    model = Panier_Produit
    template_name = 'ansade_app/Panier_Produit_form.html'
    fields = ['nom','ponderation','prix','quantite','code']


class Panier_ProduitDeleteView(DeleteView):
    model = Panier_Produit
    template_name = 'ansade_app/Panier_Produit_confirm_delete.html'
    success_url = reverse_lazy('Panier_Produit_list')

# Classe de ressource pour l'import/export des Points de Vente
class PointDeVenteResource(resources.ModelResource):
    class Meta:
        model = PointDeVente
# Fonction pour l'export des points de vente au format CSV
def export_pointsdevente_csv(request):
    pointdevente_resource = PointDeVenteResource()
    dataset = pointdevente_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pointsdevente.csv"'
    return response

# Classe de vue pour afficher la liste des points de vente
class PointDeVenteListView(ListView):
    model = PointDeVente
    template_name = 'ansade_app/pointdevente_list.html'

    
# Classe de vue pour afficher les détails d'un point de vente spécifique
class PointDeVenteDetailView(DetailView):
    model = PointDeVente
    template_name = 'ansade_app/pointdevente_detail.html'

class PointDeVenteCreateView(CreateView):
    model = PointDeVente
    template_name = 'ansade_app/pointdevente_form.html'
    fields = ['wilaya','moughataa','commune','gps_lat','gps_long','code']

class PointDeVenteUpdateView(UpdateView):
    model = PointDeVente
    template_name = 'ansade_app/pointdevente_form.html'
    fields = ['wilaya','moughataa','commune','gps_lat','gps_long','code']

class PointDeVenteDeleteView(DeleteView):
    model = PointDeVente
    template_name = 'ansade_app/pointdevente_confirm_delete.html'
    success_url = reverse_lazy('pointdevente_list')


# Classe de vue pour afficher la page d'accueil
class HomeView(TemplateView):
    template_name = 'ansade_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variable'] = 'Valeur de la variable'
        return context


def application_page(request):
    return render(request, 'ansade_app/application_page.html')
