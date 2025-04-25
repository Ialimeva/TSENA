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
    number = models.IntegerField()
    fournisseur = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'numero', null = False)
