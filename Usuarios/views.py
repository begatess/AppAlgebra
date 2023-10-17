from django.shortcuts import render
from .models import Alumno, Profesor, Grupo
from django.shortcuts import render, redirect
from .forms import Registro, AlumnoEditForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    if request.user.is_authenticated:
        user = request.user
        nombre = f"{user.nombre} {user.apellido}" 
        imagen_de_perfil = user.imagen_de_perfil
        es_profesor = request.user.es_profesor
        if es_profesor:
            profesor_id = user.id
            materias = Grupo.objects.filter(profesor__id=profesor_id)
            return render(request, 'index.html', {'es_profesor': es_profesor , 'materias': materias, 'imagen_de_perfil':imagen_de_perfil, 'nombre': nombre})
        else:
            materias_inscritas = materias_inscritas = request.user.alumno.grupos_inscritos.all()
            return render(request, 'index.html', {'es_profesor': es_profesor , 'materias': materias_inscritas, 'imagen_de_perfil':imagen_de_perfil, 'nombre': nombre})
    else:
        # El usuario necesita iniciar sesion
        return render(request, 'login.html')
   
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # El usuario es válido, iniciar sesión
            login(request, user)
            return redirect('index')  # Redirecciona a la página de inicio después del inicio de sesión exitoso
        else:
            # El usuario no es válido, mostrar mensaje de error
            error_message = "Credenciales inválidas. Por favor, intenta nuevamente."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request,"login.html")

def registro(request):
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            matricula = form.cleaned_data['matricula']
            es_alumno = form.cleaned_data['es_alumno']
            nrc = form.cleaned_data['nrc']
            img_perfil = 'img_porfile/default.png'
            if es_alumno:
                Alumno.objects.create_user(email=email, 
                                           password=password,
                                           nombre=nombre,
                                           apellido=apellido,
                                           matricula=matricula,
                                           grupo=nrc,
                                           es_profesor=False,
                                           imagen_de_perfil=img_perfil
                                           )
            else:
                Profesor.objects.create_user(email=email, 
                                            password=password,
                                            nombre=nombre,
                                            apellido=apellido,
                                            matriculaP=matricula,
                                            es_profesor=True,
                                            imagen_de_perfil=img_perfil
                                            )
                
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login_view')  # Redirecciona a la página de inicio o a donde desees después del registro exitoso
    else:
        form = Registro()
    return render(request, 'registro.html', {'form': form})

def recuperar_pass(request):
    return render(request, 'pass_reset.html')

def buscarMateria(request):
    return render(request,'input_NRC.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login_view')

def perfil(request):
    return render(request, 'perfil.html')

def editar_perfil(request):
    alumno = request.user  # Obtener el usuario actual

    if request.method == 'POST':
        form = AlumnoEditForm(request.POST, request.FILES, instance=alumno)

        if form.is_valid():
            # Verificar si el formulario se ha modificado
            if form.has_changed():
                form.save()
                messages.success(request, 'Cambios guardados exitosamente.')
            else:
                messages.info(request, 'No se registraron cambios.')

            return redirect('perfil')  # Cambia 'perfil' por la URL de la página de perfil del alumno
    else:
        form = AlumnoEditForm(instance=alumno)

    return render(request, 'editar_perfil.html', {'form': form})
