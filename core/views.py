from django.shortcuts import render, redirect
from .models import Libro, Profile
from .forms import LibroForm, CustomUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

#rest_framework
from rest_framework import viewsets
from .serializers import LibroSerializer

# Create your views here.

def index(request):
    return render(request, 'core/index.html', {})

def padrino(request):
    return render(request, 'core/pages/padrino.html', {})

def factotum(request):
    return render(request, 'core/pages/factotum.html', {})

def torero(request):
    return render(request, 'core/pages/torero.html', {})

def borges(request):
    return render(request, 'core/pages/borges.html', {})

@login_required
def listado_peliculas(request):

    user = request.user
    peliculas = Libro.objects.filter(user=user)
    data={
        'peliculas': peliculas
    }
    return render(request, 'core/listado_peliculas.html', data)

@login_required
def agregar_pelicula(request):

    data={
        'form': LibroForm()
    }

    if request.method=='POST':
        formulario = LibroForm(request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario = formulario.save(commit=False)
            formulario.user = request.user
            formulario.save()
            data['mensaje']='Libro guardado correctamente'
        data['form']=formulario

    return render(request, 'core/agregar_pelicula.html', data)

@login_required
def modificar_pelicula(request, id):
    #consultamos por id en la BD
    pelicula = Libro.objects.get(id=id)
    #creamos un objeto con una propiedad que va a contener la estructura 
    #del formulario de una pelicula
    data ={
        'form': LibroForm(instance=pelicula)
    }

    #si el metodo es de tipo POST guardamos los datos en una variable (formulario)
    if request.method=='POST':
        formulario = LibroForm(data=request.POST, instance=pelicula, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Libro modificado correctamente'
            #llenamos los campos con los datos del formulario recien actualizado
        data['form']=LibroForm(instance=Libro.objects.get(id=id))

    return render(request,'core/modificar_pelicula.html', data)

@login_required
def eliminar_pelicula(request, id):

    pelicula = Libro.objects.get(id=id)
    pelicula.delete()
    return redirect(to='listado-peliculas')

@login_required
def eliminar_pelicula_recomendaciones(request, id):

    pelicula = Libro.objects.get(id=id)
    pelicula.delete()
    return redirect(to='recomendaciones')

@login_required
def visualizar_recomendaciones(request):

    titulo = request.GET.get('titulo')
    director = request.GET.get('director')
    peliculas= Libro.objects.all()

    if 'btn-titulo' in request.GET:
        if titulo:
            peliculas = Libro.objects.filter(titulo__icontains=titulo)
    elif 'btn-director' in request.GET:
        if director:
            peliculas = Libro.objects.filter(director__icontains=director)

    data={
        'peliculas': peliculas
    }

    return render(request, 'core/recomendaciones.html', data)

def registrar_usuario(request):

    data = {
        'form': CustomUserForm(),
        'profile': ProfileForm()
    }

    if request.method=='POST':

        formulario = CustomUserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if formulario.is_valid() and profile_form.is_valid():

            new_user = formulario.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            #autenticar el usuario y redirigirlo
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            #autentificamos credenciales del usuario
            user = authenticate(username=username, password=password)
            #logueamos el usuario
            login(request, user)

            return redirect(to='index')
            
        data['form']=formulario
        data['profile']=profile_form

    return render(request, 'registration/registrar.html', data)

def perfil(request):

    user = request.user
    perfil = Profile.objects.get(user_id = user.id)
    data={      
        'perfil': perfil
    }
    return render(request, 'core/perfil.html', data)


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer