from django.db import models

# Create your models here.

class Familiar(models.Model): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)
    cumpleanios = models.DateField(blank=True, null=True)
    parentesco = models.CharField(max_length=30)
    ocupacion = models.CharField(max_length=80)

