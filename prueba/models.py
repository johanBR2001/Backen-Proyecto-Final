from django.db import models

# Create your models here.
class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    CATEGORIA_ESTADOS = (
        ("A", "ACTIVO"),
        ("I", "INACTIVO")
    )
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=CATEGORIA_ESTADOS)
    
    def __str__(self):
        return self.nombre