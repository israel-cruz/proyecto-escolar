from django.db import models
from django.contrib.auth.models import User

class Clasificacion(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Clasificaciones"

    def __str__(self):
        return self.nombre

class Material(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Materiales"

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre
        
class ListaMaterial(models.Model):
    codigo = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    descripcion = models.CharField(max_length=250,null=True, blank=True)
    cantidad = models.IntegerField()
    baja = models.BooleanField(default=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Lista de materiales"