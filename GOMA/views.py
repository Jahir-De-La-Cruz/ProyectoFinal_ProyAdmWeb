from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Post, Producto, Marca, Categoria
from .forms import ProductosForm, CreatePostForm, CategoriaForm, MarcaForm
from django.contrib import messages
from .mixins import AdminRequiredMixin, RequiredBuyMixin
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class ContactView(View):
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        })
        
        email = EmailMessage(subject, template, settings.EMAIL_HOST_USER, ['soyjahirjesua04@gmail.com'])
        
        email.fail_silently = False
        email.send()
        
        messages.success(request, 'Se ha enviado el correo exitosamente!')
        return redirect('home')

class ProductosView(View):
    def get(self, request):
        productos = Producto.objects.all()
        return render(request, 'productos.html', {
            'productos': productos
        })

class SobreNosotrosView(View):
    def get(self, request):
        return render(request, 'sobre_nosotros.html')

class ProveedoresView(View):
    def get(self, request):
        return render(request, 'proveedores.html')

class NuevoProductoView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'nuevo_producto.html', {
            'form': ProductosForm
        })

    def post(self, request):
        try:
            form = ProductosForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                if request.user.is_superuser and request.user.is_staff:
                    return redirect('index_admin')
                else:
                    return redirect('productos')
            else:
                return render(request, 'nuevo_producto.html', {
                    'form': form, 
                    'error': 'Por favor completa correctamente el formulario.'
                })
        except ValueError:
            return render(request, 'nuevo_producto.html', {
                'form' : ProductosForm,
                'error' : "Porfavor agregue datos válidos."
            })


class RegistroView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro.html', {
            'formRegister': form
        })

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if username and email and password1 and password2:
            if password1 == password2:
                try:
                    usuario = User.objects.create_user(username=username, email=email, password=password1)
                    usuario.save()
                    login(request, usuario)
                    return redirect('home')
                except IntegrityError:
                    return render(request, 'registro.html', {
                        'formRegister': UserCreationForm, 
                        'errorRegister': "El Usuario Ingresado YA Existe."
                    })
            else:
                return render(request, 'registro.html', {
                    'formRegister': UserCreationForm, 
                    'errorRegister': "Las Contraseñas NO Coinciden."
                })

        return render(request, 'registro.html', {
            'formRegister': UserCreationForm
        })

class SuperusuarioRegistroView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'superusuario_registro.html', {
            'formRegister': form
        })

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if username and password1 and password2:
            if password1 == password2:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.is_superuser = True
                    user.save()
                    return render(request, 'superusuario_registro.html', {
                        'formRegister': UserCreationForm,
                        'mensaje' : f'Superusuario {username} registrado correctamente.'
                    })
                except:
                    return render(request, 'superusuario_registro.html', {
                        'formRegister': UserCreationForm, 
                        'error': "Hubo un error al registrar el superusuario"
                    })
            else:
                return render(request, 'superusuario_registro.html', {
                    'formRegister': UserCreationForm, 
                    'error': "Las contraseñas no coinciden"
                })
        return render(request, 'superusuario_registro.html', {
            'formRegister': UserCreationForm
        })


class LoginView(View):
    def get(self, request):
        form_login = AuthenticationForm()
        error_message = request.GET.get('error')
        return render(request, 'inicio_sesion.html', {
            'formLogin': form_login,
            'errorLogin': error_message
        })

    def post(self, request):
        form_login = AuthenticationForm(request, request.POST)
        
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            Usuario = authenticate(request, username=username, password=password)
            if Usuario is not None:
                if Usuario.is_superuser and Usuario.is_staff:
                    login(request, Usuario)
                    return redirect('index_admin')
                else:
                    login(request, Usuario)
                    return redirect('home')
            else:
                return render(request, 'inicio_sesion.html', {
                    'formLogin': form_login,
                    'errorLogin': 'Usuario o contraseña incorrectos'
                })
        else:
            return render(request, 'inicio_sesion.html', {
                'formLogin': form_login,
                'errorLogin': 'Usuario o contraseña incorrectos'
            })

class CerrarSesionView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home')

class BlogView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        return render(request, 'blog.html', {
            'posts': posts
        })

class CrearNuevoBlogView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'crear_blog.html', {
            'form': CreatePostForm
        })

    def post(self, request):
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog')
        else:
            return render(request, 'crear_blog.html', {
                'form': form, 
                'error': 'Por favor, complete correctamente el formulario.'
            })

class AgregarProveedoresView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'agregar_proveedores.html', {
            'MarcaForm': MarcaForm(),
            'CategoriaForm' : CategoriaForm()
        })
    
    def post(self, request):
        if 'marca_form' in request.POST:
            formMarca = MarcaForm(request.POST)
            if formMarca.is_valid():
                formMarca = Marca.objects.create(nombre=request.POST['nombre'])
                formMarca.save()
                if request.user.is_superuser and request.user.is_staff:
                    return redirect('marcasAdmin')
                else:
                    return render(request, 'agregar_proveedores.html', {
                        'MarcaForm': MarcaForm(),
                        'CategoriaForm' : CategoriaForm(),
                        'mensajeMarca' : f'La marca {formMarca.nombre} se agrego correctamente.'
                    })
            else:
                return render(request, 'agregar_proveedores.html', {
                    'MarcaForm': MarcaForm(),
                    'CategoriaForm': CategoriaForm(),
                    'errorMarca': 'Por favor, complete correctamente el formulario de marca.'
                })
        elif 'categoria_form' in request.POST:
            formCategoria = CategoriaForm(request.POST)
            if formCategoria.is_valid():
                formCategoria = Categoria.objects.create(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'])
                formCategoria.save()
                if request.user.is_superuser and request.user.is_staff:
                    return redirect('categorias')
                else:
                    return render(request, 'agregar_proveedores.html', {
                        'MarcaForm': MarcaForm(),
                        'CategoriaForm' : CategoriaForm(),
                        'mensajeCategoria' : f'La categoria {formCategoria.nombre} se agrego correctamente.'
                    }) 
            else:
                return render(request, 'agregar_proveedores.html', {
                    'MarcaForm': MarcaForm(),
                    'CategoriaForm': CategoriaForm(),
                    'errorCategoria': 'Por favor, complete correctamente el formulario de categoría.'
                })
        return render(request, 'agregar_proveedores.html', {
            'MarcaForm': MarcaForm(),
            'CategoriaForm': CategoriaForm(),
            'error': 'No se pudo identificar el formulario enviado.'
        })

class ObtenerDetallesView(View):
    def get(self, request, producto_id):
        producto = get_object_or_404(Producto, id=producto_id)
        detalles = {
            'imagen_url': producto.imagen.url,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'marca': producto.marca.nombre,
        }
        return JsonResponse(detalles)
    
class ConfirmacionCompraView(RequiredBuyMixin, View):
    def get(self, request):
        return render(request, 'confirmar_compra.html')