from django.db import models

# Create your models here.
# class Grupo(models.Model):
#     nombre = models.CharField(max_length=100)
#     nrc = models.IntegerField()
#     profesor = models.ForeignKey('Usuarios.Profesor', on_delete=models.CASCADE)
#     imagen = models

#     def __str__(self):
#         return str(self.nrc) 



def default_imagen():
    return 'default_imagen.jpg'

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400, default="Sin descripción")
    nrc = models.IntegerField()
    profesor = models.ForeignKey('Usuarios.Profesor', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media/', default=default_imagen, null=True, blank=True)

    def __str__(self):
        return self.nombre + str(self.nrc)