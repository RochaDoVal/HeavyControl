from django.db import models, IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


cpf_validator = RegexValidator(
    regex=r'^\d{11}$',
    message='CPF inválido. Informe os 11 dígitos sem pontos ou traços.'
)

cargo_choices = [
    ("ADMINISTRADOR","ADMINISTRADOR"),
    ("OPERADOR","OPERADOR"),
    ("MOTORISTA","MOTORISTA"),
]

class CustomUser(AbstractUser):
    nome = models.CharField("Nome Completo", max_length=100, blank=True)
    cpf = models.CharField("CPF", max_length=11, unique=True,blank=True, validators=[cpf_validator])
    cargo = models.CharField("Cargo", choices=cargo_choices, max_length=30, blank=True)

    def __str__(self):
        return self.username

    def save(self,*args, **kwargs):
        if self.nome:
            self.nome = self.nome.upper()
        
        super().save(*args, **kwargs)
    
class Categoria(models.Model):
     nome = models.CharField(max_length=100, blank=True, null=False)

     def __str__(self):
        return self.nome

     def save(self,*args, **kwargs):
        if self.nome:
            self.nome = self.nome.upper()
        
        super().save(*args, **kwargs)

class Fabricante(models.Model):
     nome = models.CharField(max_length=100, blank=True,null=False)

     def __str__(self):
        return self.nome

     def save(self,*args, **kwargs):
        if self.nome:
            self.nome = self.nome.upper()
        
        super().save(*args, **kwargs)

class Modelo(models.Model):
     nome = models.CharField(max_length=100, blank=True,null=False)

     def __str__(self):
        return self.nome
     
     def save(self,*args, **kwargs):
        if self.nome:
            self.nome = self.nome.upper()
        
        super().save(*args, **kwargs)
     
class Local(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=False)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.nome.upper()
        self.full_clean()
        super().save(*args, **kwargs)

    
    
class Equipamento(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name="equipamentos")
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name="equipamentos")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="equipamentos")
    numero_serie = models.CharField("Número de Série",max_length=100,unique=True)
    horimetro_atual = models.IntegerField("Horímetro Atual",default=0)
    horimetro_manutencao = models.IntegerField("Horímetro para Manutenção",default=0)
    data_manutencao = models.DateField("Data da Última Manutenção",null=True,blank=True)
    colaborador = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="equipamentos")

    def __str__(self):
        return self.numero_serie
    

class Atividade(models.Model):
    horimetro_inicial = models.IntegerField("Horímetro Inicial",default=0)
    horimetro_final = models.IntegerField("Horímetro Final",default=0)
    abastecimento = models.IntegerField("Abastecimento Horímetro",default=0)
    litros_abastecidos = models.IntegerField("Quant de Litros Abastecidos", default=0)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    maquina = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data = models.DateField(blank=True)
    descricao = models.TextField()
    colaborador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
