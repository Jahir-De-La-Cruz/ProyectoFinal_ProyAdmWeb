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
from django.urls import path
from GOMA.views import IndexView, ProductosView, SobreNosotrosView, MarcasView, ProveedoresView, NuevoProductoView, LoginView, SuperusuarioRegistroView, RegistroView, CerrarSesionView, BlogView, CrearNuevoBlogView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="home"),
    path('productos/', ProductosView.as_view(), name="productos"),
    path('sobre-nosotros/', SobreNosotrosView.as_view(), name="sobre_nosotros"),
    path('marcas/', MarcasView.as_view(), name="marcas"),
    path('proveedores/', ProveedoresView.as_view(), name="proveedores"),
    path('nuevo-producto/', NuevoProductoView.as_view(), name="nuevo_producto"),
    path('registrar/', RegistroView.as_view(), name="registrar"),
    path('registrar_super_usuario/', SuperusuarioRegistroView.as_view(), name="registrar_super_usuario"),
    path('iniciar_sesion/', LoginView.as_view(), name="iniciar_sesion"),
    path('cerrar_sesion/', CerrarSesionView.as_view(), name="cerrar_sesion"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('crear_nuevo_blog/', CrearNuevoBlogView.as_view(), name="nuevo_blog"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
