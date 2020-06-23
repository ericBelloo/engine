
from django import forms
from apps.company.models import Company, Document
from apps.utils.models_direction import Address


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
    cp = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'CP',
               'class': 'form-control'}
    ), label='', required=True)
    state = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Estado',
               'class': 'form-control',
               'disabled': True}
    ), label='', required=False)
    city = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Municipio',
               'class': 'form-control',
               'disabled': True}
    ), label='', required=False)

    class Meta:
        model = Address
        fields = ('street_a', 'street_b', 'colony', 'number')
        widgets = {
            'colony': forms.Select(
                attrs={
                    'class': 'browser-default custom-select',
                    'required': True,
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
            'colony': '',
        }


class CompanyDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('constitutive_act', 'estate_document', 'tax_certificate', 'proof_of_address', 'bank_account', 'sat', 'employer_registration')
        widgets = {
            'constitutive_act': forms.FileInput(
                attrs={'class': 'custom-file-input',
                       'accept': 'application/pdf'
                       }),
            'estate_document': forms.FileInput(
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
