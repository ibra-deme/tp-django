from distutils.command.upload import upload
from email.mime import image
from enum import unique
from django.db import models

class Etudiant(models.Model):
    code_permanent=models.IntegerField(unique=True)
    prenom=models.CharField(max_length=100)
    nom=models.CharField(max_length=100)
    addresse=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/%Y/%m/%d",blank=True)
    date_de_naissance=models.CharField(max_length=100)
    def __str__(self):
        return self.prenom