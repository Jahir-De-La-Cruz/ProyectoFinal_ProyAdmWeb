from django.urls import path
from GOMA_admin.views import (IndexAdminView, ClientesAdminView, ComprasAdminView, CategoriasAdminView, MarcasAdminView)

urlpatterns = [
    path('index_admin/', IndexAdminView.as_view(), name='index_admin'),
    path('usuarios/', ClientesAdminView.as_view(), name='usuarios'),
    path('compras/', ComprasAdminView.as_view(), name='compras'),
    path('categorias/', CategoriasAdminView.as_view(), name='categorias'),
    path('marcasAdmin/', MarcasAdminView.as_view(), name='marcasAdmin'),
]