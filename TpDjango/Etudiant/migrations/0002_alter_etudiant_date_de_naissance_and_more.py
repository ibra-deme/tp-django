# Generated by Django 4.1.2 on 2022-10-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='date_de_naissance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]