from dataclasses import field, fields
from pyexpat import model
from django import forms
from Etudiant.models import Etudiants


class EtudiantForm(forms.ModelForm):
    class Meta:
        model=Etudiants
        fields = "__all__"