
from django.db import models
from apps.utils.models import BaseNameModel


class State(BaseNameModel):
    """ Estate """


class City(BaseNameModel):
    """ Delegacion/Municipio """
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.SET_NULL)
    cp = models.CharField(max_length=5, blank=True, null=True)  # codigo postal


class Colony(BaseNameModel):
    """ Colonia """
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)


class Address(models.Model):
    street_a = models.CharField(max_length=100)  # calle
    street_b = models.CharField(max_length=100, null=True, blank=True)  # colonia
    number = models.CharField(max_length=3, null=True, blank=True)
    colony = models.CharField(max_length=5)  # colonia