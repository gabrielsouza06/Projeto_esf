from django.db import models
from usuarios.models import Usuario
from estabelecimento.models import Estabelecimento

class Prontuario(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prontuarios_paciente')
    profissional = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prontuarios_profissional')
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name='prontuarios_estabelecimento')
    data_hora = models.DateTimeField()
    status = models.TextField()

    def __str__(self):
        return f"Prontuario de {self.paciente} - {self.data_hora}"


class Consulta(models.Model):
    data_hora = models.DateTimeField()
    status = models.TextField()

    profissional = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_profissional')
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_paciente')
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name='consultas_estabelecimento')
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE, related_name='consulta_prontuario', null=True, blank=True)

    def __str__(self):
        return f"Consulta em {self.data_hora} - Status: {self.status}"
