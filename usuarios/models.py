from django.db import models
from django.core.exceptions import ValidationError

def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError('Este campo deve conter apenas números.')

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cpf = models.CharField(max_length=14, unique=True, validators=[validate_numeric], primary_key=True)
    rg = models.CharField(max_length=15, validators=[validate_numeric])
    nome_mae = models.CharField(max_length=50)
    nome_pai = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Paciente(Pessoa):
    num_cartao_sus = models.CharField(max_length=15)

class Profissional(Pessoa):
    num_conselho = models.CharField(max_length=20)
    profissao = models.CharField(
        max_length=50,
        choices=[
            ('ENF', 'Enfermeiro(a)'),
            ('MED', 'Médico(a)'),
            ('TEC_ENF', 'Tecnólogo em Enfermagem'),
            ('DENT', 'Dentista'),
            ('FISIOTERAPEUTA', 'Fisioterapeuta'),
            ('ACS', 'Agente Comunitário de Saúde'),
            ('PSICOLOGO', 'Psicólogo(a)'),
            ('NUTRICIONISTA', 'Nutricionista'),
        ],
    )

