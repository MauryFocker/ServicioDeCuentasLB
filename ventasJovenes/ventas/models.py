from django.db import models

# Create your models here.


class Cliente(models.Model):
    codigo = models.CharField(max_length=5, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=20, null=True, blank=False)
    apellido = models.CharField(max_length=15, null=True, blank=False)
    clase = models.CharField(max_length=30, null=True, blank=True)
    telefono = models.CharField(max_length=12, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
        
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=5, unique=True, null=True, blank=True)
    descripcion = models.CharField(max_length=20, unique=True, null=False)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        order_with_respect_to='descripcion'

    def __str__(self):
        return self.descripcion