from django.db import models
# Create your models here.

class Persona(models.Model):
	primer_nombre = models.CharField(max_length=30)
	segundo_nombre = models.CharField(max_length=30)
	primer_apellido = models.CharField(max_length=30)
	segundo_apellido = models.CharField(max_length=30)
	cedula = models.IntegerField(default=0)
	fecha_de_nacimiento = models.DateField('Fecha de Nacimiento')
	telefono_casa = models.IntegerField(default=0)
	telefono_oficina = models.IntegerField(default=0)
	telefono_celular = models.IntegerField(default=0)
	correo = models.EmailField()
	tipos_genero = (
		('M','Masculino'),
		('F','Femeninoo')
	)
	genero = models.CharField(max_length=1,choices=tipos_genero)
	direccion = models.TextField(max_length=500)