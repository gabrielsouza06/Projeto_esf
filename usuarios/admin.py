from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Paciente, Profissional

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('nome_completo', 'data_nascimento', 'rua', 'num_casa', 'uf', 'cpf', 'rg', 'nome_mae', 'nome_pai')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('Informações Pessoais', {
            'fields': ('nome_completo', 'data_nascimento', 'rua', 'num_casa', 'uf', 'cpf', 'rg', 'nome_mae', 'nome_pai'),
        }),
    )
    list_display = ('username', 'nome_completo', 'email', 'is_staff')
    search_fields = ('username', 'nome_completo', 'email', 'cpf')
    ordering = ('username',)

class PacienteAdmin(CustomUserAdmin):
    fieldsets = CustomUserAdmin.fieldsets + (
        ('Informações Adicionais de Paciente', {'fields': ('num_cartao_sus',)}),
    )
    add_fieldsets = CustomUserAdmin.add_fieldsets + (
        ('Informações Adicionais de Paciente', {'fields': ('num_cartao_sus',)}),
    )

class ProfissionalAdmin(CustomUserAdmin):
    fieldsets = CustomUserAdmin.fieldsets + (
        ('Informações Adicionais de Profissional', {'fields': ('num_conselho',)}),
    )
    add_fieldsets = CustomUserAdmin.add_fieldsets + (
        ('Informações Adicionais de Profissional', {'fields': ('num_conselho',)}),
    )

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Profissional, ProfissionalAdmin)
