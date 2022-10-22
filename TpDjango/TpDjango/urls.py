"""TpDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Etudiant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('etudiant/',views.etudiant,name='acceuil'),
    path('ajouter/',views.ajouter_etudiant,name='ajout_etudiant'),
    path('ajouter/<str:pk>',views.modifier_etudiant,name='modifier_etude'),
    path('supprimer/<str:pk>',views.supprimer_etudiant,name='supprimer_etude')
]
