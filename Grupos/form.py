from django import forms
from Grupos.models import Grupo
from django import forms

class RegistroGrupo(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    nrc = forms.IntegerField()
    imagen = forms.ImageField(widget=forms.FileInput,required=False)

    class Meta:
        model = Grupo
        fields = ('nombre', 'nrc', 'imagen') 