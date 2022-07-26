from django.db import models

#Modelo de la tabla empresa.
class Empresa(models.Model):

    nombre_empresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=70)
    nit = models.PositiveBigIntegerField()
    telefono = models.PositiveBigIntegerField()
