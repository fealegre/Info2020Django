from django.db import models
from ..Usuarios.models import Usuarios

class Stalkers(models.Model):
    usuario= models.OneToOneField(Usuarios,on_delete=models.CASCADE,related_name='Stalker')

    def __str__(self):
        return self.usuario.username
