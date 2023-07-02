from django.shortcuts import render, redirect
from .models import Grupo
from .form import RegistroGrupo
from django.contrib import messages

def listar_materias(request):
    materias = Grupo.objects.all()
    return render(request, 'materias.html', {'materias': materias})

#Listar materias por profesores
def listar_materias_profesor(request):
    if request.user.is_authenticated and request.user.es_profesor:
        user = request.user
        profesor_id = user.id
        materias = Grupo.objects.filter(profesor__id=profesor_id)
    return render(request,'listar_materias.html', {'materias': materias})


def crearGrupo(request):
    if request.method == 'POST':
        form = RegistroGrupo(request.POST, request.FILES)
        if form.is_valid():
            grupo = form.save(commit=False)
            # Realiza cualquier manipulación adicional con los datos del formulario aquí
            if not grupo.imagen:  # Verificar si no se seleccionó una imagen
                grupo.imagen = 'default_imagen.jpg'  # Asignar la imagen por defecto definida en el modelo
            grupo.profesor = request.user.profesor
            grupo.save()  # Guardar el objeto Grupo en la base de datos
            return redirect('index')
    else:
        form = RegistroGrupo()
    messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
    return render(request, 'crear_grupo.html', {'form': form})

def dashboard(request, nrc):
    return render(request, 'dashboard.html', {'nrc': nrc})