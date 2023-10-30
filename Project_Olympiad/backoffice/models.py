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

"""nombre varchar
apellido varchar
email varchar/email unique?
fecha_nacimiento DATE
actividad_laboral varchar
profesion varchar
grado_educacion varchar
nacionalidad varchar
estado  varchar (creado,calificado,confirmado, aprobado,descartado)
created_at DATETIME
update_at DATETIME
created_by_id(user_id) INT
fuente (creado manualmente, pagina web, carga masiva) varchar"""

class usuarios(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    verificado=models.BooleanField(default=False)
    hash=models.CharField(max_length=40, null=True)
    hash_verificacion=models.CharField(max_length=40, null=True)
    last_login=models.DateTimeField(auto_now_add=True, null=True)
    group_id=models.IntegerField()
    active=models.BooleanField(default=True)



"""email
password varchar
created_at DATETIME
updated_at DATETIME
verificado bool
hash varchar
hash_verificacion
last_login DATETIME
group_id (1 admin, 2 ejecutivo)
active bool"""

class group(models.Model):
    nombre=models.CharField(max_length=15)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)


"""Group
id
nombre
active

1 admin
2 ejecutivo
3 personas/beneficiarios"""

class estados(models.Model):
    nombre=models.CharField(max_length=15)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

"""@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'backoffice':
        BackofficeEstado.objects.get_or_create(nombre='creado', activo=True)
        BackofficeEstado.objects.get_or_create(nombre='confirmado', activo=True)
        BackofficeEstado.objects.get_or_create(nombre='rechazado', activo=True)"""

"""
creado,aprobado,descartado
"""