from django.db import models

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)    
    #fruto da relação
    responsavel = models.OneToOneField("usuarios.Usuario", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

    
