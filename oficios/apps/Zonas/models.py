from django.db import models

# Create your models here.
class Zonas(models.Model):
    nombre= models.CharField(max_length=40)
    cp= models.IntegerField()

    def __str__(self):
        return str(self.nombre)
