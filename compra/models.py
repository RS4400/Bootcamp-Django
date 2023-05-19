from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.BigIntegerField(default=0000)

    def __str__(self):
        return f"Nombre de Proveedor: {self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField(default=0)
    stock_actual = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre de Producto: {self.nombre}"
