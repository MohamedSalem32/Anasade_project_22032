# ansade_app/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import loader
from .models import *
from django.views import View
from django.views.generic.edit import CreateView
from .forms import *
from import_export import resources
from tablib import Dataset
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
 

# Classe de ressource pour l'import/export des Produits
class ProduitResource(resources.ModelResource):
    class Meta:
        model = Produit
         
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
    return render(request, 'application_page.html')

 

# Fonction pour l'export des produits au format CSV
def export_produits_csv(request):
    produit_resource = ProduitResource()
    dataset = produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="produits.csv"'
    return response 

def import_produits_csv(request):
    result_message = None

    if request.method == 'POST':
        produit_resource = ProduitResource()
        dataset = Dataset()

        if 'myfile' not in request.FILES:
            messages.warning(request, 'Aucun fichier sélectionné.')
        else:
            new_produit_file = request.FILES['myfile']

            if not new_produit_file.name.endswith('.csv'):
                messages.error(request, 'Le fichier doit être un CSV.')
            else:
                try:
                    imported_data = dataset.load(new_produit_file.read().decode('ISO-8859-1'))
                    produit_resource.import_data(dataset, dry_run=False)
                    messages.success(request, 'Import réussi.')
                    return redirect('produit_list')
                except Exception as e:
                    messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

                result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'ansade_app/import_data.html', {'result_message': result_message})


def export_famillesproduits_csv(request):
    familleproduit_resource = FamilleProduitResource()
    dataset = familleproduit_resource.export()

    # Ajoutez ces lignes pour afficher des messages de débogage
    print("Exporting dataset:", dataset)
    print("CSV content:", dataset.csv)

    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="familleproduits.csv"'
    return response
 
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from tablib import Dataset

def import_famille_produit(request):
    result_message = None

    if request.method == 'POST':
        famille_produit_resource = FamilleProduitResource()
        dataset = Dataset()

        if 'myfile' not in request.FILES:
            messages.warning(request, 'Aucun fichier sélectionné.')
        else:
            new_familleproduit_file = request.FILES['myfile']

            if not new_familleproduit_file.name.endswith('.csv'):
                messages.error(request, 'Le fichier doit être un CSV.')
            else:
                try:
                    # Ajout de l'option format pour spécifier le format du fichier
                    imported_data = dataset.load(new_familleproduit_file.read().decode('ISO-8859-1'))
 
                    famille_produit_resource.import_data(dataset, dry_run=False)
                    messages.success(request, 'Import réussi.')
                    return redirect('familleproduit_list')
                except Exception as e:
                    messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

                result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'ansade_app/import_data.html', {'result_message': result_message})



# Fonction pour l'export des paniers au format CSV
def export_paniers_csv(request):
    panier_resource = PanierResource()
    dataset = panier_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="paniers.csv"'
    return response


def import_paniers(request):
    result_message = None

    if request.method == 'POST':
        panier_resource = PanierResource()
        dataset = Dataset()

        if 'myfile' not in request.FILES:
            messages.warning(request, 'Aucun fichier sélectionné.')
        else:
            new_panier_file = request.FILES['myfile']

            if not new_panier_file.name.endswith('.csv'):
                messages.error(request, 'Le fichier doit être un CSV.')
            else:
                try:
                    imported_data = dataset.load(new_panier_file.read().decode('ISO-8859-1'))
                    panier_resource.import_data(dataset, dry_run=False)
                    messages.success(request, 'Import réussi.')
                    return redirect('panier_list')
                    
                
                       
                except Exception as e:
                    messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

                result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'ansade_app/import_data.html', {'result_message': result_message})


# Fonction pour l'export des prix au format CSV
def export_prix_csv(request):
    prix_resource = PrixResource()
    dataset = prix_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prix.csv"'
    return response 


def import_prix(request):
    result_message = None

    if request.method == 'POST':
        prix_resource = PrixResource()
        dataset = Dataset()

        if 'myfile' not in request.FILES:
            messages.warning(request, 'Aucun fichier sélectionné.')
        else:
            new_prix_file = request.FILES['myfile']

            if not new_prix_file.name.endswith('.csv'):
                messages.error(request, 'Le fichier doit être un CSV.')
            else:
                try:
                    imported_data = dataset.load(new_prix_file.read().decode('ISO-8859-1'))
                    prix_resource.import_data(dataset, dry_run=False)
                    messages.success(request, 'Import réussi.')
                    return redirect('prix_list')
                    
                
                       
                except Exception as e:
                    messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

                result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'ansade_app/import_data.html', {'result_message': result_message})



# Fonction pour l'export des points de vente au format CSV
def export_pointsdevente_csv(request):
    pointdevente_resource = PointDeVenteResource()
    dataset = pointdevente_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pointsdevente.csv"'
    return response


def import_pointsdevente(request):
    result_message = None

    if request.method == 'POST':
        pointsdevente_resource = PointDeVenteResource()
        dataset = Dataset()

        if 'myfile' not in request.FILES:
            messages.warning(request, 'Aucun fichier sélectionné.')
        else:
            new_pointsdevente_file = request.FILES['myfile']

            if not new_pointsdevente_file.name.endswith('.csv'):
                messages.error(request, 'Le fichier doit être un CSV.')
            else:
                try:
                    imported_data = dataset.load(new_pointsdevente_file.read().decode('ISO-8859-1'))
                    pointsdevente_resource.import_data(dataset, dry_run=False)
                    messages.success(request, 'Import réussi.')
                    return redirect('pointdevente_list')
                    
                
                       
                except Exception as e:
                    messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

                result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'ansade_app/import_data.html', {'result_message': result_message})


 # Fonction pour l'export des paniers produits au format CSV
def export_paniersproduits_csv(request):
    panier_produit_resource = Panier_ProduitResource()
    dataset = panier_produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='csv')
    response['Content-Disposition'] = 'attachment; filename="paniers_produits.csv"'
    return response


def import_PanierProduits(request):
    result_message = None

    if request.method == 'POST':
        panierproduit_resource = Panier_ProduitResource()
        dataset = Dataset()

        if 'myfile' not in request.FILES:
            messages.warning(request, 'Aucun fichier sélectionné.')
        else:
            new_panierproduit_file = request.FILES['myfile']

            if not new_panierproduit_file.name.endswith('.csv'):
                messages.error(request, 'Le fichier doit être un CSV.')
            else:
                try:
                    imported_data = dataset.load(new_panierproduit_file.read().decode('utf-8'))
                    panierproduit_resource.import_data(dataset, dry_run=False)
                    messages.success(request, 'Import réussi.')
                    return redirect('Panier_Produit_list')
                    
                
                       
                except Exception as e:
                    messages.error(request, f'Une erreur s\'est produite lors de l\'import : {e}')

                result_message = list(messages.get_messages(request))  # Convert messages to a list

    return render(request, 'ansade_app/import_data.html', {'result_message': result_message})
 

from django.db.models.functions import ExtractYear
from django.db.models import Avg
from django.http import JsonResponse
from chartjs.views.lines import BaseLineChartView

class PrixEvolutionChart(BaseLineChartView):
    def get_labels(self):
        # Récupérer les années de validité des prix pour un produit spécifique et les trier
        return sorted(
            list(
                Prix.objects.filter(produit_id=self.kwargs['produit_id'])
                .annotate(year=ExtractYear('date_validite'))
                .values_list('year', flat=True)
                .distinct()
            )
        )

    def get_providers(self):
        # Récupérer les moyennes des prix pour un produit spécifique par année
        return ['Moyenne des Prix']

    def get_data(self):
        # Récupérer les moyennes des prix pour un produit spécifique par année
        moyennes = list(
            Prix.objects.filter(produit_id=self.kwargs['produit_id'])
            .annotate(year=ExtractYear('date_validite'))
            .values('year')
            .annotate(moyenne=Avg('montant'))
            .values_list('moyenne', flat=True)
        )
        return [moyennes]

    def render_to_response(self, context, **response_kwargs):
        data = {
            'labels': self.get_labels(),
            'datasets': [
                {'label': provider, 'data': values}
                for provider, values in zip(self.get_providers(), self.get_data())
            ]
        }
        return JsonResponse(data)

def prix_evolution_chart(request, produit_id):
    return render(request, 'ansade_app/prix_evolution_chart.html', {'produit_id': produit_id})



 
from django.db.models import Avg, DecimalField, Sum, F
from django.db.models.functions import Coalesce
from decimal import Decimal
 

def calculer_inpc_par_produit(annee, produit_id):
    produits = Produit.objects.filter(id=produit_id)
    resultats = []

    for produit in produits:
        prix_entries = Prix.objects.filter(
            produit=produit,
            date_validite__year=annee
        )

        somme_ponderations = Coalesce(Sum(F('panier_produit__ponderation')), Decimal(0))
        somme_produits_ponderees = Coalesce(Sum(F('montant') * F('panier_produit__ponderation'), output_field=DecimalField()), Decimal(0))

        prix_entries_aggregated = prix_entries.aggregate(
            somme_ponderations=somme_ponderations,
            somme_produits_ponderees=somme_produits_ponderees
        )

        somme_ponderations = prix_entries_aggregated['somme_ponderations']
        somme_produits_ponderees = prix_entries_aggregated['somme_produits_ponderees']

        inpc = somme_produits_ponderees / somme_ponderations if somme_ponderations > 0 else Decimal(0)

        resultats.append({
            'annee': annee,
            'produit': produit.nom,
            'inpc': inpc
        })

    return resultats



def inpc(request):
    # Liste des années disponibles
    years = [2019, 2020, 2021, 2022, 2023, 2024]  # Update this list with your available years

    # Liste des produits disponibles
    produits = Produit.objects.all()

    # Obtenez manuellement les valeurs sélectionnées par l'utilisateur
    selected_annee = request.GET.get('annee_calcul')
    selected_produit_id = request.GET.get('produit')

    # Si les valeurs ne sont pas fournies dans la requête, utilisez une valeur par défaut
    if not selected_annee:
        selected_annee = '2023'  # Valeur par défaut si l'année n'est pas spécifiée

    if not selected_produit_id:
        selected_produit_id = produits.first().id  # Utilisez le premier produit par défaut si aucun n'est spécifié

    # Assurez-vous que la valeur n'est pas une chaîne vide avant de convertir en entier
    if selected_annee and selected_annee != '':
        selected_annee = int(selected_annee)

    # Calculer l'indice des prix annuel pour chaque produit
    indices_prix_annuels = calculer_inpc_par_produit(selected_annee, selected_produit_id)

    # Faites quelque chose avec les indices, comme les passer au contexte pour l'affichage dans le modèle
    context = {
        'indices_prix_annuels': indices_prix_annuels,
        'years': years,
        'produits': produits,
        'selected_annee': selected_annee,
        'selected_produit': selected_produit_id
    }

    return render(request, 'ansade_app/inpc.html', context)
