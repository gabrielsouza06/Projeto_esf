from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Pessoa(AbstractBaseUser, models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField(unique=True, verbose_name='Email')
    senha = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'sobrenome']

    def __str__(self):
        return self.nome