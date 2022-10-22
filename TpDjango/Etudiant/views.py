from multiprocessing import context
from django.shortcuts import render,redirect
from Etudiant.models import Etudiants
from Etudiant.forms import EtudiantForm
def etudiant(request):
    etudiants=Etudiants.objects.all()
    return render(request,'etudiant/acceuil.html',{'etudiants':etudiants})


def ajouter_etudiant(request):
    form=EtudiantForm()
    if request.method=='POST':
        form=form=EtudiantForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/etudiant')
    context={'form':form}        
    return render(request,'etudiant/ajouter.html',context)


def modifier_etudiant(request,pk):
    etude=Etudiants.objects.get(id=pk)
    form=EtudiantForm(instance=etude)
    if request.method=='POST':
        form=form=EtudiantForm(request.POST,instance=etude)
        if form.is_valid():
            form.save()  
            return redirect('/etudiant')
    context={'form':form}        
    return render(request,'etudiant/ajouter.html',context)

def supprimer_etudiant(request,pk):
    etud=Etudiants.objects.get(id=pk)
    if request.method=='POST':
        etud.delete()
        return redirect('/etudiant')
    context={'item':etud}    
    return render(request,'etudiant/supprimer.html',context)
# Create your views here.
