from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Create your models here.

class beneficiarios(models.Model):
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    fecha_nacimiento=models.DateTimeField(auto_now_add=False)
    nacionalidad=models.CharField(max_length=15)
    email=models.EmailField()
    telefono=models.CharField(max_length=15)
    pais_residencia=models.CharField(max_length=15)
    grado_educacion=models.CharField(max_length=15, null=True)
    actividad_laboral=models.CharField(max_length=15, null=True)
    profesion=models.CharField(max_length=15, null=True)
    estado=models.CharField(max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    created_by=models.IntegerField()
    fuente=models.CharField(max_length=15)


class estados(models.Model):
    nombre=models.CharField(max_length=15)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

"""
creado,aprobado,descartado
"""