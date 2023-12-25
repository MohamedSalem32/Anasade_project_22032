# ansade_app/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import loader
from .models import Produit, FamilleProduit, Panier, Prix, Ponderation, PointDeVente
from django.views.generic.edit import CreateView
from .forms import FamilleProduitForm

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
    fields = ['nom', 'description', 'famille','prix']

class ProduitUpdateView(UpdateView):
    model = Produit
    template_name = 'ansade_app/produit_form.html'
    fields = ['nom', 'description', 'famille']

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'ansade_app/produit_confirm_delete.html'
    success_url = reverse_lazy('produit_list')

# Classe de vue pour afficher la liste des familles de produits


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
    fields = ['nom', 'description']

class PanierUpdateView(UpdateView):
    model = Panier
    template_name = 'ansade_app/panier_form.html'
    fields = ['nom', 'description']

class PanierDeleteView(DeleteView):
    model = Panier
    template_name = 'ansade_app/panier_confirm_delete.html'
    success_url = reverse_lazy('panier_list')    

# Classe de vue pour afficher la liste des prix
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
    fields = ['montant', 'produit']

class PrixUpdateView(UpdateView):
    model = Prix
    template_name = 'ansade_app/prix_form.html'
    fields = ['montant', 'produit']

class PrixDeleteView(DeleteView):
    model = Prix
    template_name = 'ansade_app/prix_confirm_delete.html'
    success_url = reverse_lazy('prix_list')

# Classe de vue pour afficher la liste des pondérations
class PonderationListView(ListView):
    model = Ponderation
    template_name = 'ansade_app/ponderation_list.html'

# Classe de vue pour afficher les détails d'une pondération spécifique
class PonderationDetailView(DetailView):
    model = Ponderation
    template_name = 'ansade_app/ponderation_detail.html'

class PonderationCreateView(CreateView):
    model = Ponderation
    template_name = 'ansade_app/ponderation_form.html'
    fields = ['nom', 'valeur']

class PonderationUpdateView(UpdateView):
    model = Ponderation
    template_name = 'ansade_app/ponderation_form.html'
    fields = ['nom', 'valeur']

class PonderationDeleteView(DeleteView):
    model = Ponderation
    template_name = 'ansade_app/ponderation_confirm_delete.html'
    success_url = reverse_lazy('ponderation_list')

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
    fields = ['nom', 'adresse']

class PointDeVenteUpdateView(UpdateView):
    model = PointDeVente
    template_name = 'ansade_app/pointdevente_form.html'
    fields = ['nom', 'adresse']

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
