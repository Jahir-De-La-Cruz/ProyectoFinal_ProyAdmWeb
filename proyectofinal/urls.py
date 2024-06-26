"""
URL configuration for proyectofinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from GOMA.views import (IndexView, ProductosView, SobreNosotrosView, ProveedoresView, NuevoProductoView, 
AgregarProveedoresView, LoginView, SuperusuarioRegistroView, RegistroView, CerrarSesionView, BlogView, 
CrearNuevoBlogView, BuscarProductosView, ConfirmacionCompraView, ContactView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="home"),
    path('productos/', ProductosView.as_view(), name="productos"),
    path('buscar_productos/', BuscarProductosView.as_view(), name='buscar_productos'),
    path('sobre_nosotros/', SobreNosotrosView.as_view(), name="sobre_nosotros"),
    path('proveedores/', ProveedoresView.as_view(), name="proveedores"),
    path('nuevo_producto/', NuevoProductoView.as_view(), name="nuevo_producto"),
    path('nuevo_proveedor/',AgregarProveedoresView.as_view(), name="nuevo_proveedor"),
    path('registrar/', RegistroView.as_view(), name="registrar"),
    path('registrar_super_usuario/', SuperusuarioRegistroView.as_view(), name="registrar_super_usuario"),
    path('iniciar_sesion/', LoginView.as_view(), name="iniciar_sesion"),
    path('cerrar_sesion/', CerrarSesionView.as_view(), name="cerrar_sesion"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('crear_nuevo_blog/', CrearNuevoBlogView.as_view(), name="nuevo_blog"),
    path('confirmar_compra/', ConfirmacionCompraView.as_view(), name='confirmar_compra'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('', include('GOMA_admin.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
