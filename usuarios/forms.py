from django import forms
from .models import Paciente, Profissional, Usuario
from django.contrib.auth.forms import UserCreationForm

UF_CHOICES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username', 'email',
            'nome_completo', 'data_nascimento', 'rua', 'num_casa', 'uf',
            'cpf', 'rg', 'nome_mae', 'nome_pai', 'password1'
        ]
        widgets = {
            'uf': forms.Select(choices=UF_CHOICES),
        }


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['username', 'password', 'nome_completo', 'data_nascimento', 'rua', 'num_casa', 'uf', 'cpf', 'rg', 'nome_mae', 'nome_pai', 'num_cartao_sus']

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['username', 'password', 'nome_completo', 'data_nascimento', 'rua', 'num_casa', 'uf', 'cpf', 'rg', 'nome_mae', 'nome_pai', 'num_conselho']
