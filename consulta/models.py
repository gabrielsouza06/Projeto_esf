from django.db import models
from django.contrib.auth.models import User

class Pessoa(User):
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=10)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=8)
    cpf = models.IntegerField(max_length=14)
    rg = models.IntegerField(max_length=15)
    nome_mae = models.CharField(max_length=50)
    nome_pai = models.CharField(max_length=50)

class Paciente(Pessoa):
    num_cartao_sus = models.CharField(max_length=15)


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
        verbose_name="Profissão",
    )

    def __str__(self):
        return f"{self.nome} ({self.profissao})"