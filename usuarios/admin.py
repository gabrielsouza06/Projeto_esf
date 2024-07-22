from django.contrib import admin
from .models import Paciente, Profissional

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'num_cartao_sus')
    search_fields = ('nome_completo', 'cpf', 'num_cartao_sus')
    list_filter = ('cidade', 'uf')

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'num_conselho', 'profissao')
    search_fields = ('nome_completo', 'cpf', 'num_conselho', 'profissao')
    list_filter = ('cidade', 'uf', 'profissao')
