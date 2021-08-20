from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


class Usuarios(AbstractUser):
	Trabajador=models.BooleanField(default=False)
	address=models.CharField(max_length=60,null=True)
	phone=models.BigIntegerField(null=True)
	
	#Obtener los datos del usuario para mostrarlos
	def ObtenerDatos(self):
		cositas={'Usuario':self.username,'Nombre':self.first_name,'Apellido':self.last_name,'Email':self.email,
		'Direccion':self.address,'Telefono':self.phone}
		
		return cositas
		
	#Obtener el pk si el usuario es un trabajador o un stalker
	def ObtenerPk(self):
		if(self.Trabajador):
			return self.Worker.pk
		return self.Stalker.pk

	def ObtenerPerfil(self):
		if(self.Trabajador):
			return self.Worker
		return self.Stalker