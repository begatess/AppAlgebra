from django.shortcuts import render, redirect
from .models import Grupo
from .form import RegistroGrupo, BuscarMateriaForm, GrupoInscripcionForm
from django.contrib import messages

#Vistas generales
def listar_materias(request):
    materias = Grupo.objects.all()
    form = BuscarMateriaForm()

    if request.method == "POST":
        form = BuscarMateriaForm(request.POST)
        if form.is_valid():
            nrc_nombre = form.cleaned_data['nrc']

            if nrc_nombre:
                # Realizar la búsqueda por NRC o nombre (puedes personalizar la lógica de búsqueda)
                materias = materias.filter(nrc=nrc_nombre) | materias.filter(nombre__icontains=nrc_nombre)

    return render(request, 'materias.html', {'materias': materias, 'form': form})

## Vistas Profesores
#Crea un grupo Profesor
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

#Listar materias por profesores
def listar_materias_profesor(request):
    if request.user.is_authenticated and request.user.es_profesor:
        user = request.user
        profesor_id = user.id
        materias = Grupo.objects.filter(profesor__id=profesor_id)

         # Agregar conteo de estudiantes en cada grupo
        for materia in materias:
            materia.numero_estudiantes = materia.alumnos_inscritos.count()
            
    return render(request,'listar_materias_profesores.html', {'materias': materias})

## Vistas Alumnos
#Listar materias por alumnos
def listar_materias_alumno(request):
    if request.user.is_authenticated:
        user = request.user
        #materias = Grupo.objects.filter(profesor__id=profesor_id)
    return render(request,'listar_materias_alumno.html', {})

def dashboard(request, nrc):
    return render(request, 'dashboard.html', {'nrc': nrc})

#Registro a materia
def detalles_materia(request, nrc):
    materia = Grupo.objects.get(nrc=nrc)
    return render(request, 'detalles_materia.html', {'materia': materia})

def inscripcion_materia(request, nrc):
    try:
        materia = Grupo.objects.get(nrc=nrc)
        request.user.alumno.grupos_inscritos.add(materia)
        return redirect('index') 
    except Grupo.DoesNotExist:
        return render(request,"index")

def mis_materias (request):
    if request.user.is_authenticated:
        user = request.user
        materias = user.alumno.grupos_inscritos.all()   
    return render(request, 'mis_materias.html',{'user': user, 'materias': materias})