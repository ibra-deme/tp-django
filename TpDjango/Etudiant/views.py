from django.shortcuts import render
from Etudiant.models import Etudiant
def etudiant(request):
    etudiants=Etudiant.objects.all()
    return render(request,'etudiant/acceuil.html',{'etudiants':etudiants})

# Create your views here.
