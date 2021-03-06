from django.db import models
from apps.utils.models_direction import BaseNameModel, Address


class Document(models.Model):
    constitutive_act = models.FileField(upload_to='company/constitutive_act/')  # acta constitutiva
    estate_document = models.FileField(upload_to='company/state/')  # Hacienda
    tax_certificate = models.FileField(upload_to='company/tax_certificate/')  # Cedula Fiscal
    proof_of_address = models.FileField(upload_to='company/proof_of_address/')  # Comprobante Direccion
    bank_account = models.FileField(upload_to='company/bank_account/')  # Cuenta de banco
    sat = models.FileField(upload_to='company/sat/')  # sat
    employer_registration = models.FileField(upload_to='company/employer_registration/')  # registro patronal


class Company(BaseNameModel):
    business_name = models.CharField(max_length=100, null=True, blank=True)  # razon social
    rfc = models.CharField(max_length=50)
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.CASCADE)  # direccion
    document = models.ForeignKey(Document, blank=True, null=True, on_delete=models.CASCADE)  # documentos
