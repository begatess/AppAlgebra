from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Alumno
from Grupos.models import Grupo
from django import forms
from .models import Alumno, Profesor

class Registro(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    matricula = forms.IntegerField()
    nrc = forms.ModelChoiceField(queryset=Grupo.objects.all(), required=False)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    es_alumno = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'id': 'es_alumno'}))

    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'email', 'password', 'password2',  'matricula', 'nrc') 