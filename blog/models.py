from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=50)
