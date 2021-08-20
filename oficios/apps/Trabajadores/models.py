from django.db import models
from ..Usuarios.models import Usuarios
from ..Zonas.models import Zonas

class Rubros(models.Model):
    nombre=models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Trabajadores(models.Model):
    usuario= models.OneToOneField(Usuarios,on_delete=models.CASCADE,related_name='Worker')
    promedio= models.FloatField(default=0)
    especialidad= models.CharField(max_length=50)
    certificado = models.ImageField(upload_to='Trabajadores',null=True,blank=True)
    rubro = models.ForeignKey(Rubros,null=True,on_delete=models.SET_NULL,related_name='filtro_rubro')
    zonas = models.ManyToManyField(Zonas,related_name='Opera',blank=True)

    def __str__(self):
        return self.usuario.username
