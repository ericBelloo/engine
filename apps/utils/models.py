
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
