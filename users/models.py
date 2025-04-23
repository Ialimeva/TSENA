from django.db import models
from django.contrib.auth.models import User


""" roles des utilisateurs """
class role(models.Model):
    nom_role = models.CharField(max_length = 15)

""" User and role connex """
class role_user_connex(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'role')
    role = models.OneToOneField(role, on_delete = models.CASCADE, related_name = 'user')

""" Numero de telephone """
class Number(models.Model):
    number = models.IntegerField(max_length = 9)

""" Numero et fournisseur connex """
class fournisseur_numero(models.Model):
    fournisseur = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'numero')
    number = models.OneToOneField(Number, on_delete = models.CASCADE, related_name = 'fournisseur')