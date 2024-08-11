from django.db import models

class Consulta(models.Model):
    data_hora = models.DateTimeField()
    status = models.TextField()

    
    def __str__(self):
        return f"Consulta em {self.data_hora} - Status: {self.status}"
