from django.shortcuts import render, redirect
from users.models import User, role, role_user_connex, Number, fournisseur_numero
from django.contrib import messages

# Create your views here.

""" Admin """
def admin_register(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        username = request.POST['username']
        email = request.POST['email']
        mot_de_passe = request.POST['password1']
        comfirmation = request.POST['password2']

        require_fileds = {
            'Nom': nom,
            'Prénom' : prenom,
            "Nom d'utilisateur" : username,
            'Email': email,
            'Mot de passe': mot_de_passe,
            'Comfirmation': comfirmation,
        }

        
        for field, value in require_fileds.items():
            if not value or value.isspace():
                messages.error(request, f'Le champ {field} est obligatoire')
                

        if mot_de_passe == comfirmation:
            try:
                new_admin = User.objects.create_superuser(
                    first_name = nom,
                    last_name = prenom,
                    username = username,
                    email = email,
                    password = mot_de_passe,
                )
                new_admin.is_superuser = True
                new_admin.is_staff = True
                new_admin.is_active = True

                admin_role = role.objects.get(nom_role = 'Admin')

                user_role = role_user_connex.objects.create(user = new_admin, role = admin_role)            
                
                if user_role.is_valid():
                    user_role.save()

                messages.success(request, 'Compte admin créer')
            finally:
                return render(request, 'admin/register_admin.html')
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas!')        
    return render(request, 'admin/register_admin.html')


""" Fournisseur """
def fournisseur_register(request):
    if request.method == 'POST':
        nom_tsena = request.POST['nom_tsena']
        email = request.POST['email']
        number = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        required_fields = {
            'Nom du Tsena': nom_tsena,
            'Email': email,
            'Numéro de Téléphone': number,
            'Mot de passe': password1,
            'Comformation': password2,
        }

        for field, value in required_fields.items():
            if value is None or value.isspace():
                messages.error(request, f'Le champ {field} est obligatoire')

        if password1 == password2:
            try:
                new_fournisseur = User.objects.create_user(
                    username = nom_tsena,
                    email = email,
                    password = password1,
                )
                    
                role_instance = role.objects.get(role = 'Fournisseur')

                fournisseur_role = role_user_connex.objects.create(user = new_fournisseur, role = role_instance)
                fournisseur_role.save()

                new_number = Number.objects.create(number = number)
            
                new_number.save()

                new_fournisseur_number = fournisseur_numero.objects.create(
                    fournisseur = new_fournisseur,
                    number = new_number,
                )
            
                new_fournisseur_number.save()
            except Exception as e:
                messages.error(request, f'Erreur: {e}')
                return render(request, 'fournisseur/register_fournisseur.html')
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas!')  
    return render(request, 'fournisseur/register_fournisseur.html')