from django.forms import ModelForm
from .models import Comentarios
from django.utils import timezone
from ..Trabajadores.models import Trabajadores
from ..Stalkers.models import Stalkers

class ComentariosForm(ModelForm):
    class Meta:
        model = Comentarios
        fields =['descripcion']

#Redefinicion del save para que devuelva la instancia y no guarde en la base de datos instant
#Hasta que yo se lo diga
    def save(self,commit=False):
        comentario = super().save(commit)
        comentario.fecha_pub = timezone.now()
        return comentario