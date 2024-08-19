from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Profissional, Paciente

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
            'username': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-user'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control form-control-user', 'type': 'date'}),
            'rua': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'num_casa': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'uf': forms.Select(choices=UF_CHOICES, attrs={'class': 'form-control form-control-user'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'rg': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-user'}),
        }

class ProfissionalForm(UserCreationForm):
    class Meta:
        model = Profissional
        fields = [
            'username', 'email',
            'nome_completo', 'data_nascimento', 'rua', 'num_casa', 'uf',
            'cpf', 'rg', 'nome_mae', 'nome_pai', 'password1', 'num_conselho'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-user'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control form-control-user', 'type': 'date'}),
            'rua': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'num_casa': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'uf': forms.Select(choices=UF_CHOICES, attrs={'class': 'form-control form-control-user'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'rg': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-user'}),
            'num_conselho': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }


class PacienteForm(UserCreationForm):
    class Meta:
        model = Paciente
        fields = [
            'username', 'email',
            'nome_completo', 'data_nascimento', 'rua', 'num_casa', 'uf',
            'cpf', 'rg', 'nome_mae', 'nome_pai', 'password1', 'num_cartao_sus'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-user'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control form-control-user', 'type': 'date'}),
            'rua': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'num_casa': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'uf': forms.Select(choices=UF_CHOICES, attrs={'class': 'form-control form-control-user'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'rg': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-user'}),
            'num_cartao_sus': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }
