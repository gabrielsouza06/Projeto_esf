from django.db import models

class Vacina(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Remedio(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

