from django.db import models

# Create your models here.

class Insumo (models.Model):
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 100)
    quantidade = models.IntegerField()

   