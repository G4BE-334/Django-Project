from django.contrib import admin

# Register your models here.

from .models import Cliente, Grupo, Recomendacao
admin.site.register(Cliente)
admin.site.register(Grupo)
admin.site.register(Recomendacao)