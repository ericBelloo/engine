
from django import forms
from apps.company.models import Company, Document, CompanyNDA
from apps.utils.models import Address, State


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'rfc')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de la empresa',
                    'class': 'form-control'
                }),
            'rfc': forms.TextInput(
                attrs={
                    'placeholder': 'R.F.C',
                    'class': 'form-control'
                })
        }
        labels = {
            'name': '',
            'business_name': '',
            'rfc': ''
        }


class CompanyAddressForm(forms.ModelForm):
    """ Formulario para la direccion de la empresa """

    state = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Estado',
               'class': 'form-control'}), label='')
    city = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Municipio',
               'class': 'form-control'}
    ), label='')
    colony = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Colonia',
               'class': 'form-control'}
    ), label='')

    class Meta:
        model = Address
        fields = ('street_a', 'street_b', 'cp', 'number')
        widgets = {
            'cp': forms.TextInput(
                attrs={
                    'placeholder': 'Codigo Postal',
                    'class': 'form-control'
                }),
            'street_a': forms.TextInput(
                attrs={
                    'placeholder': 'Calle',
                    'class': 'form-control'
                }),
            'street_b': forms.TextInput(
                attrs={
                    'placeholder': 'Y Calle',
                    'class': 'form-control'
                }),
            'number': forms.TextInput(
                attrs={
                    'placeholder': 'Número',
                    'class': 'form-control'
                })
        }
        labels = {
            'street_a': '',
            'street_b': '',
            'cp': '',
        }


class CompanyDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('constitutive_act', 'estate', 'tax_certificate', 'proof_of_address', 'bank_account', 'sat', 'employer_registration')
        widgets = {
            'constitutive_act': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       }),
            'estate': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       }),
            'tax_certificate': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       }),
            'proof_of_address': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       }),
            'bank_account': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       }),
            'sat': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       }),
            'employer_registration': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       })
        }
        labels = {
            'constitutive_act': '',
            'estate': '',
            'tax_certificate': '',
            'proof_of_address': '',
            'bank_account': '',
            'sat': '',
            'employer_registration': ''
        }


class CompanyNDAForm(forms.ModelForm):
    class Meta:
        model = CompanyNDA
        fields = ('cmg', 'dgj', 'dgq', 'gnp', 'ngm', 'tmg')
        widgets = {
            'cmg': forms.FileInput(),
            'dgj': forms.FileInput(),
            'dgq': forms.FileInput(),
            'gnp': forms.FileInput(),
            'ngm': forms.FileInput(),
            'tmg': forms.FileInput()
        }
