from django.contrib import admin
from .models import Vacina, Remedio

@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'quantidade')

@admin.register(Remedio)
class RemedioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'quantidade')
