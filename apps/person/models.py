from django.contrib.auth.models import User
from django.db import models
from apps.company.models import Company


class Document(models.Model):
    ine = models.FileField(upload_to='person/ine/')
    power_letter = models.FileField(upload_to='person/power_letter/')


class Person(models.Model):
    telephone_number = models.CharField(max_length=12, null=True, blank=True)
    phone_number = models.CharField(max_length=10)
    rfc = models.CharField(max_length=13)
    document = models.ForeignKey(Document, blank=True, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)


PETITION_CHOICE = (
    ('cmg', 'cmg'),
    ('dgj', 'dgj'),
    ('dgq', 'dgq'),
    ('gnp', 'gnp'),
    ('ngm', 'ngm'),
    ('tmg', 'tmg'),
)


class PetitionNDA(models.Model):
    petition_type = models.CharField(choices=PETITION_CHOICE, blank=True, null=True, max_length=10)
    file = models.FileField(upload_to='person/nda/', null=True, blank=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL)


