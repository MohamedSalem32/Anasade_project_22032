# ansade_project/urls.py
from django.contrib import admin
from django.urls import path, include
from ansade_app.views import HomeView

# Listes des URLs pour l'application ansade_app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ansade/', include('ansade_app.urls')),  # Inclure les URLs de votre application ansade_app

    # Chemin pour afficher la page d'accueil
    path('', HomeView.as_view(), name='home'),
]
