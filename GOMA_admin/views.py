from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from GOMA.models import Producto, Compra, Marca, Categoria, Proveedor
from GOMA.mixins import AdminRequiredMixin, UserRequiredMixin
from GOMA.forms import ProductosForm

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
            'producto' : producto,
            'form' : form
        })
        
    def post(self, request, producto_id):
        try:
            producto = get_object_or_404(Producto, pk=producto_id)
            form = ProductosForm(request.POST, instance=producto)
            form.save()
            return redirect('index_admin')
        except ValueError:
            return render(request, 'editar_productos.html', {
                'producto' : producto,
                'form' : form,
                'error' : "Hubo un error al actualizar el producto"
            })
        
class ClientesAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        clientes = User.objects.all()
        return render(request, 'clientes.html', {
            'clientes': clientes
        })

class ComprasAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        clientes_con_compras = User.objects.prefetch_related('compra_set__compraproducto_set').all()
        return render(request, 'compras.html', {
            'clientes_con_compras': clientes_con_compras
        })
    
class MarcasAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        marcas = Marca.objects.all()
        return render(request, 'marcasAdmin.html', {
            'marcas' : marcas
        })
    
class CategoriasAdminView(LoginRequiredMixin, AdminRequiredMixin, View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, 'categorias.html', {
            'categorias' : categorias
        })    
        
# class UserListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
#     model = User
#     template_name = 'usuarios.html'
#     context_object_name = 'usuarios'

# class UserCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
#     model = User
#     fields = ['username', 'email', 'password']
#     template_name = 'usuario_form.html'
#     success_url = reverse_lazy('user_list')

# class UserUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
#     model = User
#     fields = ['username', 'email']
#     template_name = 'usuario_form.html'
#     success_url = reverse_lazy('user_list')

# class UserDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
#     model = User
#     success_url = reverse_lazy('user_list')

# class ClienteListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
#     model = User
#     template_name = 'clientes.html'
#     context_object_name = 'clientes'

# class ClienteCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
#     model = User
#     fields = ['nombre', 'email', 'telefono']
#     template_name = 'cliente_form.html'
#     success_url = reverse_lazy('cliente_list')

# class ClienteUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
#     model = User
#     fields = ['nombre', 'email', 'telefono']
#     template_name = 'cliente_form.html'
#     success_url = reverse_lazy('cliente_list')

# class ClienteDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
#     model = User
#     success_url = reverse_lazy('cliente_list')