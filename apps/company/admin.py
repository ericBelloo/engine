from django.contrib import admin
from apps.company.models import Company, Document

# Register your models here.
admin.site.register(Company)
admin.site.register(Document)