from django.contrib import admin
from Etudiant.models import *

class affichage(admin.ModelAdmin):
    list_display=('code_permanent','nom','prenom','addresse','image','date_de_naissance')

admin.site.register(Etudiants,affichage)

# Register your models here.
