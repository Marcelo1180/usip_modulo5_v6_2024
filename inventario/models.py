from django.db import models
from .validators import validar_par, validation_categoria
from django.core.validators import EmailValidator


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, validators=[validation_categoria,])

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("reporte_cantidad", "Visualizar reporte de cantidad"),
            ("reporte_detalle", "Visualizar reporte de detalle"),
        ]

class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'

class Producto(models.Model):
    # nombre = models.CharField(max_length=100, validators=[EmailValidator(message="El email no es valido")])
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_par,])
    stock = models.IntegerField()
    unidades = models.CharField(max_length=2, choices=ProductUnits.choices, default=ProductUnits.UNITS)
    disponible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre