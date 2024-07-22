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

class Reserva(models.Model):
    remedio = models.ForeignKey(Remedio, on_delete=models.CASCADE)
    nome_pessoa = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    data_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome_pessoa} - {self.remedio.nome}'

