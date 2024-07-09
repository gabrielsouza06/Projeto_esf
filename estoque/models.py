from django.db import models

class Vacina(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

class remedio(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()