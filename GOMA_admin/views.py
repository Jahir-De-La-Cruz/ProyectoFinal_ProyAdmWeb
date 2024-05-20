from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from GOMA.models import Producto, Compra, Marca, Categoria
from GOMA.mixins import AdminRequiredMixin
from GOMA.forms import ProductosForm, CategoriaForm, MarcaForm

# Create your views here.
class IndexAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        productos = Producto.objects.all()
        return render(request, 'indexAdmin.html', {
            'productos' : productos
        })
        
class EditarProductosView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        form = ProductosForm(instance=producto)
        return render(request, 'editar_productos.html', {
            'producto': producto,
            'form': form
        })
        
    def post(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        form = ProductosForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f"El producto {producto.nombre} se actualizó correctamente")
            return redirect('index_admin')
        else:
            return render(request, 'editar_productos.html', {
                'producto': producto,
                'form': form,
                'error': "Hubo un error al actualizar el producto"
            })
            
class EliminarProductosView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        producto.delete()
        return redirect('index_admin')
                
class ClientesAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        clientes = User.objects.all()
        return render(request, 'clientes.html', {
            'clientes': clientes
        })
                    
class EliminarClientesView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, cliente_id):
        cliente = get_object_or_404(User, pk=cliente_id)
        cliente.delete()
        return redirect('usuarios')

class ComprasAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        clientes_con_compras = User.objects.prefetch_related('compra_set__compraproducto_set').all()
        compras = Compra.objects.all()
        return render(request, 'compras.html', {
            'clientes_con_compras': clientes_con_compras,
            'compras': compras
        })
    
class MarcasAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        marcas = Marca.objects.all()
        return render(request, 'marcasAdmin.html', {
            'marcas': marcas
        })

class EditarMarcasView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, marca_id):
        marca = get_object_or_404(Marca, pk=marca_id)
        form = MarcaForm(instance=marca)
        return render(request, 'editar_marcas.html', {
            'marca': marca,
            'form': form
        })

    def post(self, request, marca_id):
        marca = get_object_or_404(Marca, pk=marca_id)
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, f"La marca {marca.nombre} se actualizó correctamente")
            return redirect('marcasAdmin')
        else:
            return render(request, 'editar_marcas.html', {
                'marca': marca,
                'form': form,
                'error': "Hubo un error al actualizar la marca"
            })

class EliminarMarcasView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, marca_id):
        marca = get_object_or_404(Marca, pk=marca_id)
        marca.delete()
        messages.success(request, f"La marca {marca.nombre} se eliminó correctamente")
        return redirect('marcasAdmin')
    
class CategoriasAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, 'categorias.html', {
            'categorias' : categorias
        })
        
class EditarCategoriasView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, categoria_id):
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        form = CategoriaForm(instance=categoria)
        return render(request, 'editar_categorias.html', {
            'categoria': categoria,
            'form': form
        })
                
    def post(self, request, categoria_id):
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, f"La categoria {categoria.nombre} se actualizó correctamente")
            return redirect('categorias')
        else:
            return render(request, 'editar_categorias.html', {
                'categoria': categoria,
                'form': form,
                'error': "Hubo un error al actualizar la categoria"
            })
            
class EliminarCategoriasView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request, categoria_id):
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        categoria.delete()
        messages.success(request, f"La marca {categoria.nombre} se eliminó correctamente")
        return redirect('categorias')