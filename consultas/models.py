from django.db import models
from usuarios.models import Usuario
from estabelecimento.models import Estabelecimento

class Consulta(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_paciente')
    profissional = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_profissional')
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name='consultas_estabelecimento')
    data_hora = models.DateTimeField()
    status = models.TextField()

    def __str__(self):
        return f"Consulta em {self.data_hora} - Status: {self.status}"

class Prontuario(models.Model):  # Corrigido para 'Prontuario' em vez de 'Pronturario'
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prontuarios_paciente')
    profissional = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prontuarios_profissional')
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name='prontuarios_estabelecimento')
    data_hora = models.DateTimeField()
    status = models.TextField()
