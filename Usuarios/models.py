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
    imagen_de_perfil = models.ImageField(upload_to='media/', default='img_porfile/default.png' , null=True, blank=True)
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
    grupos_inscritos = models.ManyToManyField(Grupo, related_name='alumnos_inscritos', blank=True)

class Profesor(Usuario):
    matriculaP = models.IntegerField()