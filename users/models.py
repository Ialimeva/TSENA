from django.db import models
from django.contrib.auth.models import User


""" roles des utilisateurs """
class role(models.Model):
    nom_role = models.CharField(max_length = 15)

""" User and role connex """
class role_user_connexAdmin(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'roleAdmin')
    role = models.ForeignKey(role, on_delete = models.CASCADE, related_name = 'roleAdmin')

class role_user_connexFournisseur(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'roleFournisseur')
    role = models.ForeignKey(role, on_delete = models.CASCADE, related_name = 'roleFournisseur')

class role_user_connexClient(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'roleClient')
    role = models.ForeignKey(role, on_delete = models.CASCADE, related_name = 'roleClient')
