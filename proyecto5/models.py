from django.db import models

# Create your models here.

class Persona(models.Model):

    DNI=models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    SEXO_OPCIONES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    sexo=models.CharField(max_length=1, choices=SEXO_OPCIONES,verbose_name="Sexo")
    fecha_nacimiento=models.DateField()
    direccion = models.CharField(max_length=200, blank=True, default="")
    telefono=models.CharField(max_length=15, blank=True, default="")
    correo=models.EmailField()