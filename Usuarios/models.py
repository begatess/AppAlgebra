from asyncio import AbstractServer
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from Grupos.models import Grupo
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('es_profesor', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    es_profesor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    objects = UsuarioManager()

    def __str__(self):
        return self.nombre +' '+ self.apellido

class Alumno(Usuario):
    matricula = models.PositiveSmallIntegerField()
    grupo = models.ForeignKey('Grupos.Grupo', on_delete=models.CASCADE, default="1")

class Profesor(Usuario):
    matriculaP = models.IntegerField()

# class Usuario(AbstractUser):
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     correo_electronico = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     es_profesor = models.BooleanField(default=False)
    
#     class Meta:
#         abstract = True
    
#     def __str__(self):
#         etiqueta = "{0} ({1})"
#         if(self.es_profesor == True):
#             tipo = "Profesor"
#         else:
#             tipo = "Alumno"
#         return etiqueta.format(self.nombre, tipo)
    
    
# class Alumno(models.Model):
#     user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
#     matricula = models.IntegerField()
#     grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='alumnos_grupo')
    
# class Profesor(models.Model):
    # matriculaP = models.IntegerField()
    # user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    # grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='profesores_grupo')

# class Grupo(models.Model):
#     nombre = models.CharField(max_length=100)
#     nrc = models.IntegerField()
#     profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre
