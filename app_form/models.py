from django.db import models

class Formulario(models.Model):
    data = models.DateField()
    atividade = models.CharField(max_length=100)
    horimetro_final = models.IntegerField()
    horimetro_abastecimento = models.IntegerField()
    quantidade_litros = models.IntegerField()

    def __str__(self):
        return f'{self.atividade}'