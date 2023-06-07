from django.contrib import admin
from django.urls import path,include
import json
from gestionIncendi.views import accueil
from categorie_incident.views import urgent
from categorie_incident.views import moinurgent
from propos.views import propos
from contact.views import connexion
from contact.views import inscription
from  services.views import communication
from  services.views import historique



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('', accueil,name="accueil"),
    path('urgent/',urgent, name="urgent"),
    path('moinurgent/',moinurgent, name="moinurgent"),
    path('propos/',propos, name="propos"),
    path('connexion/',connexion,name="connexion"),
    path('inscription/',inscription, name="inscription"),
    path('communication/',communication,name="communication"),
    path('historique/',historique,name="historique"),
    
]

endpoint ='http://127.0.0.1:8000/api'