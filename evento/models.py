from django.db import models
from insumo.models import Insumo
from voluntario.models import Voluntario

# Create your models here.

class Evento (models.Model):
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 100)
    data = models.DateField()
    local = models.CharField(max_length = 50)
    insumo = models.ManyToManyField(Insumo, blank = True)
    voluntario = models.ManyToManyField(Voluntario, blank = True)