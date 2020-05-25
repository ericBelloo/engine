
"""
 Abstract class
"""
from django.db import models


class BaseNameModel(models.Model):
    name = models.CharField(max_length=100)

    create_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class State(BaseNameModel):
    """ Estate """


class City(BaseNameModel):
    """ Municipio """
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.SET_NULL)


class Colony(BaseNameModel):
    """ Colonia """
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)


class CP(models.Model):
    cp = models.CharField(max_length=5, primary_key=True)
    colony = models.ForeignKey(Colony, blank=True, null=True, on_delete=models.SET_NULL)


class Address(models.Model):
    street_a = models.CharField(max_length=100)  # calle
    street_b = models.CharField(max_length=100, null=True, blank=True)  # colonia
    number = models.CharField(max_length=3, null=True, blank=True)
    cp = models.CharField(max_length=5)  # codigo postal