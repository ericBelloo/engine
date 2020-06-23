
from django import forms
from django.contrib.auth.models import User

from apps.person.models import Person, Document, PetitionNDA


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electrónico',
                    'class': 'form-control'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Contraseña',
                    'class': 'form-control'
                }
            ),
        }
        labels = {
            'username': '',
            'password': '',
        }


class UserForm(forms.ModelForm):
    """
    Username: el nombre de usuario sera su correo electronico
    """
    second_last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Apellido Materno', 'class': 'form-control'}
    ), label='', max_length=50, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirme su contraseña', 'class': 'form-control'}
    ), label='', max_length=50, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')
        widgets = {
            'username': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electrónico',
                    'class': 'form-control'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Contraseña',
                    'class': 'form-control'
                }),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                    'class': 'form-control',
                    'required': True
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido Paterno',
                    'class': 'form-control',
                    'required': True
                }),
        }
        labels = {
            'username': '',
            'password': '',
            'first_name': '',
            'last_name': ''
        }


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('telephone_number', 'phone_number', 'rfc')
        widgets = {
            'telephone_number': forms.TextInput(
                attrs={'placeholder': 'Num. Telefono',
                       'class': 'form-control only-numbers'
                       }),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Num. Celular',
                       'class': 'form-control only-numbers'
                       }),
            'rfc': forms.TextInput(
                attrs={'placeholder': 'R.F.C',
                       'class': 'form-control'
                       })
        }
        labels = {
            'telephone_number': '',
            'phone_number': '',
            'rfc': ''
        }


class PersonDocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('ine', 'power_letter')
        widgets = {
            'ine': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       }),
            'power_letter': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       })
        }
        labels = {
            'ine': '',
            'power_letter': ''
        }


class PersonPetitionNDAForm(forms.ModelForm):
    cmg = forms.CharField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'accept': 'application/pdf'}), required=False)
    dgj = forms.CharField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'accept': 'application/pdf'}), required=False)
    gnp = forms.CharField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'accept': 'application/pdf'}), required=False)
    dgq = forms.CharField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'accept': 'application/pdf'}), required=False)
    tmg = forms.CharField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'accept': 'application/pdf'}), required=False)
    ngm = forms.CharField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'accept': 'application/pdf'}), required=False)

    class Meta:
        model = PetitionNDA
        fields = ('petition_type', 'file', 'person')
