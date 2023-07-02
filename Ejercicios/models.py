from django.db import models

# Create your models here.

class Ejercicio(models.Model):
    enunciado = models.TextField()
    solucion = models.TextField()

class Ejercicios(models.Model):
    descripcion = models.CharField(max_length=100)
    ejercicios = models.ManyToManyField(Ejercicio)