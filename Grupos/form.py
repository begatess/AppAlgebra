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

class BuscarMateriaForm(forms.Form):
    nrc = forms.CharField(
        label="Buscar por NRC o nombre",
        required=False,  # Permite dejar el campo vacío
        widget=forms.TextInput(attrs={'placeholder': 'NRC o nombre'}),
    )

class GrupoInscripcionForm(forms.Form):
    grupos_seleccionados = forms.ModelMultipleChoiceField(
        queryset=Grupo.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )