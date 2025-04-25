from django.shortcuts import render, redirect
from users.models import User, role, role_user_connex, Number
from django.contrib import messages
from users.forms import AdminRegistration, FournisseurRegister

# Create your views here.

""" Admin """
def admin_register(request):
    if request.method == 'POST':
        admin_instance = AdminRegistration(request.POST)
        if admin_instance.is_valid():
            admin_instance.save()
            
            role_instance = role.objects.get(nom_role = 'admin') 

            admin_role = role_user_connex.objects.create(user = admin_instance, role = role_instance)
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
        number = request.POST['number']
        
        if instance.is_valid():
            instance.save()

            fournisseur_number = Number.objects.create(fournisseur = instance, number = number)

            fournisseur_number.save()
    else:
        instance = FournisseurRegister()

    context = {
        'form': instance
    }
    return render(request, 'fournisseur/register_fournisseur.html', context)