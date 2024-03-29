from django import forms
from .models import Producto, Post

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'cantidad', 'disponibilidad', 'marca', 'categoria', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el Nombre del Producto'
            }),
            'precio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el Precio del Producto'
            }),
            'cantidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la Cantidad del Producto'
            }),
            'disponibilidad': forms.CheckboxInput(attrs={
                'class': 'form-control',
            }),
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la Marca del Producto'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Seleccione la Categoria del Producto'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
        error_messages = {
            'imagen': {
                'required': 'Por favor, cargue una imagen para el producto.',
            },
        }
        
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título del Post'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el contenido del Post'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
        error_messages = {
            'image': {
                'required': 'Por favor, cargue una imagen para el post.',
            },
        }