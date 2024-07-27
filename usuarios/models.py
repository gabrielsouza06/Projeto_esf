from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True, blank=True)
    rua = models.CharField(max_length=255)
    num_casa = models.IntegerField()
    uf = models.CharField(max_length=2)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    nome_mae = models.CharField(max_length=255)
    nome_pai = models.CharField(max_length=255, blank=True, null=True)
    is_paciente = models.BooleanField(default=False)
    is_profissional = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Nome personalizado para o relacionamento reverso
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='usuario'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permission_set',  # Nome personalizado para o relacionamento reverso
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuario'
    )

    def __str__(self):
        return self.nome_completo

class Profissional(Usuario):
    num_conselho = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

class Paciente(Usuario):
    num_cartao_sus = models.CharField(max_length=15, unique=True)
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
