
from django import forms
from apps.person.models import Person, Document


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('name', 'last_name', 'second_last_name', 'email', 'telephone_number', 'phone_number', 'rfc')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido Paterno'}),
            'second_last_name': forms.TextInput(attrs={'placeholder': 'Apellido Materno'}),
            'email': forms.TextInput(attrs={'placeholder': 'Correo electronico'}),
            'telephone_number': forms.TextInput(attrs={'placeholder': 'Num. Telefono'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Num. Celular'}),
            'rfc': forms.TextInput(attrs={'placeholder': 'R.F.C'})
        }
        labels = {
            'name': '',
            'last_name': '',
            'second_last_name': '',
            'email': '',
            'telephone_number': '',
            'phone_number': '',
            'rfc': ''
        }


class PersonDocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('ine', 'power_letter')
        widgets = {
            'ine': forms.FileInput(),
            'power_letter': forms.FileInput()
        }
        labels = {
            'ine': '',
            'power_letter': ''
        }
