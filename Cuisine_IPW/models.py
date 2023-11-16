from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Frigo(models.Model):
    id_frigo = models.IntegerField(default=0, primary_key=True)
    #aliments_dispo = CharField
    username = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)


    def __str__(self):
        return self.id_frigo

class Photo_plat(models.Model):
    id_photo = models.IntegerField(default=0, primary_key=True)
    chemin_photo = models.ImageField(upload_to='media/photo_plat')
    username = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    id_service = models.ForeignKey('Service', on_delete=models.CASCADE)
    id_avis = models.ForeignKey('Avis', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_photo

class Recette(models.Model):
    popularite = [(1), (2), (3), (4), (5)]
    id_recette = models.IntegerField(default=0, primary_key=True)
    nom_recette = models.CharField(max_length=100)
    instructions = models.CharField(max_length=200)
    popularite = models.IntegerField(default=0)
    temps_preparation = models.IntegerField(default=0)
    temps_cuisson = models.IntegerField(default=0)
    id_ingredient = models.ForeignKey('Ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_recette


class Avis(models.Model):
    note = [(1,1), (2,2), (3,3), (4,4), (5,5)]
    id_avis = models.IntegerField(default=0, primary_key=True)
    commentaire = models.CharField(max_length=200)
    note = models.IntegerField(default=3, choices=note)  # RETRAVAILLER !!
    username = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    id_service = models.ForeignKey('Service', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_avis


class Service(models.Model):
    id_service = models.IntegerField(default=0, primary_key=True)
    nom_service = models.CharField(max_length=10)
    origine = models.CharField(max_length=20)
    id_recette = models.ForeignKey('Recette', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_service

class Ingredients(models.Model):
    id_ingredient = models.IntegerField(default=0, primary_key=True)
    nom_ingredient = models.CharField(max_length=50)
    unite = models.CharField(max_length=50)
    id_frigo = models.ForeignKey('Frigo', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_ingredient