from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError('Este campo deve conter apenas números.')

class Pessoa(User):
    nome_completo = models.CharField(max_length=100)
    #data_nascimento = models.DateField()
    #TODO: "table usuario_pessoa has no column named data_nascimento" não comsegui resouver o erro 
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)  # Geralmente o campo UF tem 2 caracteres
    cpf = models.CharField(max_length=14, unique=True, validators=[validate_numeric], primary_key=True)
    rg = models.CharField(max_length=15, unique=True, validators=[validate_numeric])
    nome_mae = models.CharField(max_length=50)
    nome_pai = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_completo


class Paciente(Pessoa):
    num_cartao_sus = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_completo

class Profissional(Pessoa):
    num_conselho = models.CharField(max_length=20)
    profissao = models.CharField(
        max_length=50,
        choices=[
            ('ENF', 'Enfermeiro(a)'),
            ('MED', 'Médico(a)'),
            ('TEC_ENF', 'Tecnólogo em Enfermagem(a)'),
            ('DENT', 'Dentista'),
            ('FISIOTERAPEUTA', 'Fisioterapeuta'),
            ('ACS', 'Agente Comunitário de Saúde'),
            ('PSICOLOGO', 'Psicólogo(a)'),
            ('NUTRICIONISTA', 'Nutricionista'),
        ],
    )

    def __str__(self):
        return self.nome_completo