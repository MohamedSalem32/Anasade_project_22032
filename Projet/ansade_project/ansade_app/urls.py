# ansade_app/urls.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse
from .models import Produit, FamilleProduit, Panier, Prix, Ponderation, PointDeVente

# Importez la classe HomeView
from django.views import View
from django.http import HttpResponse
from django.template import loader

from django.urls import path
from .views import *

urlpatterns = [
    # Chemin pour afficher la liste des produits
    path('produits/', ProduitListView.as_view(), name='produit_list'),
    # Chemin pour afficher les détails d'un produit spécifique
    path('produits/<int:pk>/', ProduitDetailView.as_view(), name='produit_detail'),
    path('produits/ajouter/', ProduitCreateView.as_view(), name='produit_create'),
    path('produits/modifier/<int:pk>/', ProduitUpdateView.as_view(), name='produit_update'),
    path('produits/supprimer/<int:pk>/', ProduitDeleteView.as_view(), name='produit_delete'),

    
    # Chemin pour afficher les détails d'une famille de produit spécifique
    path('famillesproduits/<int:pk>/', FamilleProduitDetailView.as_view(), name='familleproduit_detail'),
    path('famillesproduits/', FamilleProduitListView.as_view(), name='familleproduit_list'),
    path('famillesproduits/<int:pk>/', FamilleProduitDetailView.as_view(), name='familleproduit_detail'),
    path('famillesproduits/ajouter/', FamilleProduitCreateView.as_view(), name='ajouter_familleproduit'),
    path('famillesproduits/modifier/<int:pk>/', FamilleProduitUpdateView.as_view(), name='modifier_familleproduit'),
    path('famillesproduits/supprimer/<int:pk>/', FamilleProduitDeleteView.as_view(), name='supprimer_familleproduit'),
    
    
    # Chemin pour afficher la liste des paniers
    path('paniers/', PanierListView.as_view(), name='panier_list'),
    # Chemin pour afficher les détails d'un panier spécifique
    path('paniers/<int:pk>/', PanierDetailView.as_view(), name='panier_detail'),
    path('paniers/ajouter/', PanierCreateView.as_view(), name='panier_create'),
    path('paniers/modifier/<int:pk>/', PanierUpdateView.as_view(), name='panier_update'),
    path('paniers/supprimer/<int:pk>/', PanierDeleteView.as_view(), name='panier_delete'),

    # Chemin pour afficher la liste des prix
    path('prix/', PrixListView.as_view(), name='prix_list'),
    # Chemin pour afficher les détails d'un prix spécifique
    path('prix/<int:pk>/', PrixDetailView.as_view(), name='prix_detail'),
     path('prix/ajouter/', PrixCreateView.as_view(), name='prix_create'),
    path('prix/modifier/<int:pk>/', PrixUpdateView.as_view(), name='prix_update'),
    path('prix/supprimer/<int:pk>/', PrixDeleteView.as_view(), name='prix_delete'),

    # Chemin pour afficher la liste des pondérations
    path('ponderations/', PonderationListView.as_view(), name='ponderation_list'),
    # Chemin pour afficher les détails d'une pondération spécifique
    path('ponderations/<int:pk>/', PonderationDetailView.as_view(), name='ponderation_detail'),
    path('ponderations/ajouter/', PonderationCreateView.as_view(), name='ponderation_create'),
    path('ponderations/modifier/<int:pk>/', PonderationUpdateView.as_view(), name='ponderation_update'),
    path('ponderations/supprimer/<int:pk>/', PonderationDeleteView.as_view(), name='ponderation_delete'),
    
    # Chemin pour afficher la liste des points de vente
    path('pointdeventes/', PointDeVenteListView.as_view(), name='pointdevente_list'),
    # Chemin pour afficher les détails d'un point de vente spécifique
    path('pointdeventes/<int:pk>/', PointDeVenteDetailView.as_view(), name='pointdevente_detail'),
    path('pointdeventes/ajouter/', PointDeVenteCreateView.as_view(), name='pointdevente_create'),
    path('pointdeventes/modifier/<int:pk>/', PointDeVenteUpdateView.as_view(), name='pointdevente_update'),
    path('pointdeventes/supprimer/<int:pk>/', PointDeVenteDeleteView.as_view(), name='pointdevente_delete'),
    
    # ... autres chemins

    # Chemin pour afficher la page d'accueil
    path('accueil/', HomeView.as_view(), name='home'),
]
