from django.db import models
from ..Trabajadores.models import Trabajadores
from ..Stalkers.models import Stalkers
# Create your models here.

class Comentarios(models.Model):
    fecha_pub = models.DateField()
    descripcion = models.TextField()
    trabajador = models.ForeignKey(Trabajadores,on_delete=models.CASCADE,related_name='comentado')
    stalker = models.ForeignKey(Stalkers,on_delete=models.CASCADE,related_name='comento')

    def __str__(self):
        return 'Comentario'+str(self.pk)