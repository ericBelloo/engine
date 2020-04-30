
from django import forms
from apps.company.models import Company, Document, CompanyNDA
from apps.utils.models import Address, State


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'business_name', 'rfc')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre de la empresa'}),
            'business_name': forms.TextInput(attrs={'placeholder': 'Razón social'}),
            'rfc': forms.TextInput(attrs={'placeholder': 'R.F.C'})
        }
        labels = {
            'name': '',
            'business_name': '',
            'rfc': ''
        }


class CompanyAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street_a', 'cp', 'colony', 'number')
        widgets = {
            'street_a': forms.TextInput(attrs={'placeholder': 'Calle'}),
            'cp': forms.TextInput(attrs={'placeholder': 'Codigo Postal'}),
            'colony': forms.TextInput(attrs={'placeholder': 'Colony'}),
            'number': forms.TextInput(attrs={'placeholder': 'Número'})
        }
        labels = {
            'street_a': '',
            'cp': '',
            'colony': '',
        }


class CompanyDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('constitutive_act', 'estate', 'tax_certificate', 'proof_of_address', 'bank_account', 'sat', 'employer_registration')
        widgets = {
            'constitutive_act': forms.FileInput(),
            'estate': forms.FileInput(),
            'tax_certificate': forms.FileInput(),
            'proof_of_address': forms.FileInput(),
            'bank_account': forms.FileInput(),
            'sat': forms.FileInput(),
            'employer_registration': forms.FileInput()
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
