from django.db import models

class Maquinas(models.Model):
    nome = models.CharField(max_length=100)
    numero_serie = models.IntegerField()
    modelo = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    horimetro_atual = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    ultima_manutencao_horimetro = models.CharField(max_length=100)
    data_ultima_manutencao = models.DateField()

    def __str__(self):
        return f"{self.nome}"

