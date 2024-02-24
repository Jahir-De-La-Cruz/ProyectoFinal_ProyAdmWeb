from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return "Marca: " + self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    
    def __str__(self):
        return "Categoria: " + self.nombre + ", Descripción: " + self.descripcion

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    marcas = models.ManyToManyField(Marca)
    
    def __str__(self):
        return "Proveedor: " + self.nombre + ", Contacto: Telefono " + self.telefono

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + " - " + "Cantidad: " + str(self.cantidad) + " unidades"

class Compra(models.Model):
    nombreCompleto = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    productos = models.ManyToManyField(Producto, through='CompraProducto')
    precioFinal = models.DecimalField(max_digits=10, decimal_places=2)
    fechaCompra = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Compro: " + self.nombreCompleto + ", el día " + str(self.fechaCompra.date())

class CompraProducto(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"Cliente: {self.compra.nombreCompleto} - Producto: {self.producto.nombre} - {self.cantidad} unidades"