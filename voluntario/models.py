from django.db import models

# Create your models here.

class Voluntario (models.Model):
    cpf = models.CharField(max_length = 50, unique = True)
    nome = models.CharField(max_length = 50)
    sexo = models.BooleanField()
    email = models.EmailField()
    dataNascimento = models.DateField()
    funcao = models.CharField(max_length = 50)
    telefone = models.IntegerField()