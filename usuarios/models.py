from django.contrib.auth.models import User
from django.db import models

class Usuario(User):
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True, blank=True)
    rua = models.CharField(max_length=255)
    num_casa = models.IntegerField()
    uf = models.CharField(max_length=2)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    nome_mae = models.CharField(max_length=255)
    nome_pai = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome_completo

class Profissional(Usuario):
    num_conselho = models.CharField(max_length=50)


class Paciente(Usuario):
    num_cartao_sus = models.CharField(max_length=15, unique=True)
