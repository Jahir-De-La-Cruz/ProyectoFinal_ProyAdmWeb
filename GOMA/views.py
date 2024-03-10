from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Post, Producto
from .forms import ProductosForm, CreatePostForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def productos(request):
    productos = Producto.objects.filter(disponibilidad=True)
    return render(request, 'productos.html', {
        'productos' : productos
    })

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def marcas(request):
    return render(request, 'marcas.html')

def proveedores(request):
    return render(request, 'proveedores.html')

@login_required
def nuevo_producto(request):
    if request.method == 'GET':
        return render(request, 'nuevo_producto.html', {
            'form' : ProductosForm
        })
    else:
        try:
            form = ProductosForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('productos')
            else:
                return render(request, 'nuevo_producto.html', {
                    'form' : ProductosForm,
                    'error' : 'Porfavor completa correctamente el formulario.'
                })
        except ValueError:
            return render(request, 'crear_blog.html', {
                'form' : ProductosForm,
                'error' : 'Porfavor ingrese datos validos.'
            })

# Vista que permite tanto logearse como registrarse en el sitio web, con autenticación y validaciones
def registrar(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'formRegister' : UserCreationForm,
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
                        'formRegister' : UserCreationForm,
                        'formLogin' : AuthenticationForm,
                        'errorRegister': "El Usuario Ingresado YA Existe."
                    })
            else:
                return render(request, 'registro.html', {
                    'formRegister' : UserCreationForm,
                    'formLogin' : AuthenticationForm,
                    'errorRegister': "Las Contraseñas NO Coinciden."
                })
        else:
            Usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if Usuario is None:
                return render(request, 'registro.html', {
                    'formRegister' : UserCreationForm,
                    'formLogin' : AuthenticationForm,
                    'errorLogin': 'Usuario o contraseña incorrectos'
                })
            else:
                login(request, Usuario)
                return render(request, 'index.html', {
                    'usuario': Usuario
                })
                 
# Vista que destruye la sesión que se haya iniciado
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

# Vista que retorna el blog y envia como parametro una variable que contiene un array con todos los posts en la db
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {
        'posts' : posts
    })
    
# Vista para crear blogs
def crear_nuevo_blog(request):
    if request.method == 'GET':
        return render(request, 'crear_blog.html', {
            'form' : CreatePostForm
        })
    else:
        try:
            form = CreatePostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog')
            else:
                return render(request, 'crear_blog.html', {
                    'form' : CreatePostForm,
                    'error' : 'Por favor, complete correctamente el formulario.'
                })
        except ValueError:
            return render(request, 'crear_blog.html', {
                'form' : CreatePostForm,
                'error' : 'Porfavor ingrese datos validos.'
            })