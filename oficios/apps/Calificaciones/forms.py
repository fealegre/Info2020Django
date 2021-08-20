from django.forms import ModelForm, RadioSelect
from .models import Calificaciones

class CalificacionesForm(ModelForm):
    class Meta:
        model=Calificaciones
        fields=['calificacion']
        ordering=['calificacion']
        empty=None
        widgets = {
            'calificacion': RadioSelect(),
        }
    def save(self,commit=False):
        calificacion=super().save(commit)
        return calificacion
