from django.db import models
from Usuarios.models import Alumno
# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField()
    alumnos = models.ManyToManyField(Alumno, through='EntregaTarea')

class EntregaTarea(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='entregas/')
    fecha_entrega = models.DateTimeField(auto_now_add=True)