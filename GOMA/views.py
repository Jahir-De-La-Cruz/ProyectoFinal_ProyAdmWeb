from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registrar(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form' : UserCreationForm,
            'formLogin' : AuthenticationForm
        })
    else:
        if 'password1' in request.POST and 'password2' in request.POST:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    Usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    Usuario.save()
                    login(request, Usuario)
                    return render(request, 'index.html', {
                        'usuario': Usuario,
                    })
                except IntegrityError:
                    return render(request, 'registro.html', {
                        'form' : UserCreationForm,
                        'formLogin' : AuthenticationForm,
                        'error': "El Usuario Ingresado YA Existe."
                    })
            else:
                return render(request, 'registro.html', {
                    'form' : UserCreationForm,
                    'formLogin' : AuthenticationForm,
                    'error': "Las Contraseñas NO Coinciden."
                })
        else:
            Usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if Usuario is None:
                return render(request, 'iniciar_sesion.html', {
                    'form' : UserCreationForm,
                    'formLogin' : AuthenticationForm,
                    'error': 'Usuario o contraseña incorrectos'
                })
            else:
                login(request, Usuario)
                return render(request, 'index.html', {
                    'usuario': Usuario
                })
            
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def blog(request):
    return render(request, 'blog.html', {
        'posts' : Post
    })