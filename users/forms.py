from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class AdminRegistration(UserCreationForm):
    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    # Custom labels and error messages for the for fields
    def __init__(self, *args, **kwargs):
        # Create a copy of UserCreationForm by calling it with super() and putting that copy inside of Admin register form
        super().__init__(*args, **kwargs)


        # Now we have our own copy of UserCreationForm that we can modify to our liking and use it in AdminRegistration
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        
        self.fields['first_name'].label = 'Nom:'
        self.fields['first_name'].error_messages = {
            'required': 'Le champ nom est obligatoire',
        }
        self.fields['last_name'].label = 'Prénom:'
        self.fields['last_name'].error_messages = {
            'required': 'Le champ prénom est obligatoire',
        }
        self.fields['username'].label = 'Nom d\'utilisateur:'
        self.fields['username'].error_messages = {
            'required': 'Le champ nom d\'utilisateur est obligatoire',
            'unique': 'Le nom d\'utilisateur n\'est plus disponible',
        }
        self.fields['email'].label = 'Email:'
        self.fields['email'].error_messages = {
            'required': 'Le champ email est obligatoire',
        }
        self.fields['password1'].label = 'Mot de passe:'
        self.fields['password1'].error_messages = {
            'required': 'Le champ mot de passe est obligatoire',
            'password_too_short': 'Le mot de passe doit contenir au moins 8 caractères',
            'password_too_common': 'Le mot de passe est trop commun',
            'password_entirely_numeric': 'Le mot de passe ne peut pas être uniquement numérique',
        }
        self.fields['password2'].label = 'Comfirmez le mot de passe:'
        self.fields['password2'].error_messages = {
            'required': 'Le champ comfirmation est obligatoire',
            'password_too_short': 'Le mot de passe doit contenir au moins 8 caractères',
            'password_too_common': 'Le mot de passe est trop commun',
            'password_entirely_numeric': 'Le mot de passe ne peut pas être uniquement numérique',
            'password_mismatch': 'Les deux mots de passe ne correspondent pas',

        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('L\'adresse email est déja associé à un compte')
        return email
    

# Fournisseur form
class FournisseurRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required =  True

        self.fields['username'].label = 'Votre Tsena'
        self.fields['username'].error_messages = {
            'required': 'Le champ Tsena est obligatoire',
            'unique': 'Le Tsena n\'est plus disponible'
        }
        self.fields['email'].label = 'Email'
        self.fields['email'].error_messages = {
            'required': 'Le champ email est obligatoire',
            'unique': 'L\'adresse email est déja associé à un Tsena'
        }
        self.fields['password1'].label = 'Mot de passe'
        self.fields['password1'].error_messages = {
            'required': 'Le champ mot de passe est obligatoire',
            'password_too_short': 'Le mot de passe doit contenir au moins 8 caractères',
        }
        self.fields['password2'].label = 'Comfirmez le mot de passe:'
        self.fields['password2'].error_messages = {
            'required': 'Le champ comfirmation est obligatoire',
            'password_too_short': 'Le mot de passe doit contenir au moins 8 caractères',
            'password_too_common': 'Le mot de passe est trop commun',
            'password_entirely_numeric': 'Le mot de passe ne peut pas être uniquement numérique',
            'password_mismatch': 'Les deux mots de passe ne correspondent pas',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('L\'adresse email est déja associé à un Tsena')
        return email
