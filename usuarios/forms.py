from django import forms
from .models import Paciente, Profissional

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['username', 'password', 'nome_completo', 'data_nascimento', 'rua', 'num_casa', 'uf', 'cpf', 'rg', 'nome_mae', 'nome_pai', 'num_cartao_sus']

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['username', 'password', 'nome_completo', 'data_nascimento', 'rua', 'num_casa', 'uf', 'cpf', 'rg', 'nome_mae', 'nome_pai', 'num_conselho']
