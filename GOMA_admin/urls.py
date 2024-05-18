from django.urls import path
from GOMA_admin.views import (IndexAdminView, ClientesAdminView, ComprasAdminView, CategoriasAdminView, MarcasAdminView, EditarProductosView, EliminarProductosView, EliminarClientesView, EditarCategoriasView, EliminarCategoriasView, EditarMarcasView, EliminarMarcasView)

urlpatterns = [
    path('index_admin/', IndexAdminView.as_view(), name='index_admin'),
    path('usuarios/', ClientesAdminView.as_view(), name='usuarios'),
    path('compras/', ComprasAdminView.as_view(), name='compras'),
    path('categorias/', CategoriasAdminView.as_view(), name='categorias'),
    path('marcasAdmin/', MarcasAdminView.as_view(), name='marcasAdmin'),
    path('editar_producto/<int:producto_id>', EditarProductosView.as_view(), name='editar_producto'),
    path('eliminar_producto/<int:producto_id>', EliminarProductosView.as_view(), name='eliminar_producto'),
    path('eliminar_cliente/<int:cliente_id>', EliminarClientesView.as_view(), name='eliminar_cliente'),
    path('editar_categoria/<int:categoria_id>', EditarCategoriasView.as_view(), name='editar_categoria'),
    path('eliminar_categoria/<int:categoria_id>', EliminarCategoriasView.as_view(), name='eliminar_categoria'),
    path('editar_marca/<int:marca_id>', EditarMarcasView.as_view(), name='editar_marca'),
    path('eliminar_marca/<int:marca_id>', EliminarMarcasView.as_view(), name='eliminar_marca')
]