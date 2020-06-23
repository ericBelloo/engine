from django.contrib import admin
from apps.person.models import Person, Document, PetitionNDA

# Register your models here.
admin.site.register(Person)
admin.site.register(Document)
admin.site.register(PetitionNDA)