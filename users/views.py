from django.shortcuts import render, redirect
from users.models import role, role_user_connexAdmin, role_user_connexFournisseur, role_user_connexClient
from django.contrib import messages
from users.forms import AdminRegistration, FournisseurRegister, ClientRegister

# Create your views here.

""" Admin """
def admin_register(request):
    if request.method == 'POST':
        admin_instance = AdminRegistration(request.POST)
        if admin_instance.is_valid():
            admin = admin_instance.save()

            role_instance = role.objects.get(nom_role = 'Admin') 

            admin_role = role_user_connexAdmin.objects.create(user = admin , role = role_instance)
            admin_role.save()
    else:
        admin_instance = AdminRegistration()
            
    context = {
        'admin_form' : admin_instance
    }       
    return render(request, 'admin/register_admin.html', context)


""" Fournisseur """
def fournisseur_register(request):
    if request.method == 'POST':
        instance = FournisseurRegister(request.POST)
        
        if instance.is_valid():
            user = instance.save()
            

            role_instance = role.objects.get(nom_role = 'Fournisseur') 

            fournisseur_role = role_user_connexFournisseur.objects.create(user = user, role = role_instance)
            fournisseur_role.save()
    else:
        instance = FournisseurRegister()

    context = {
        'form': instance
    }  
    return render(request, 'fournisseur/register_fournisseur.html', context)


def client_register(request):
    if request.method == 'POST':
        instance = ClientRegister(request.POST)
        
        if instance.is_valid():
            user = instance.save()
            

            role_instance = role.objects.get(nom_role = 'Client') 

            client_role = role_user_connexClient.objects.create(user = user, role = role_instance)
            client_role.save()
    else:
        instance = ClientRegister()

    context = {
        'form': instance
    }  
    return render(request, 'client/register_client.html', context)