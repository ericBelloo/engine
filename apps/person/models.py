from django.db import models
from apps.utils.models import BaseNameModel
from apps.company.models import Company, CompanyNDA


class Document(models.Model):
    ine = models.FileField(upload_to='person/ine/')
    power_letter = models.FileField(upload_to='person/power_letter/')


class Person(BaseNameModel):
    last_name = models.CharField(max_length=50)
    second_last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    telephone_number = models.CharField(max_length=12, null=True, blank=True)
    phone_number = models.CharField(max_length=10)
    rfc = models.CharField(max_length=12)
    document = models.ForeignKey(Document, blank=True, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    nda = models.ForeignKey(CompanyNDA, null=True, blank=True, on_delete=models.SET_NULL)



