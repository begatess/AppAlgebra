from django.db import models

# Create your models here.
class Opcion(models.Model):
    texto = models.CharField(max_length=100)
    
class Pregunta(models.Model):
    enunciado = models.TextField()
    respuesta = models.CharField(max_length=100)
    opciones = models.ManyToManyField(Opcion)

class Examen(models.Model):
    titulo = models.CharField(max_length=100)
    preguntas = models.ManyToManyField(Pregunta)
