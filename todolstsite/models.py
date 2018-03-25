from django.db import models

class Usuario(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=15)
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)

	def __getNombreCompleto__(self):
		return self.nombre+' '+self.apellido


class Tarea(models.Model):
	usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
	titulo = models.CharField(max_length=100)
	descripcion = models.TextField()
	estado = models.BooleanField(default=0)

	def marcarRealizado(self):
		self.estado = 1
		self.save()
		
	def __getTitulo__(self):
		return self.titulo
