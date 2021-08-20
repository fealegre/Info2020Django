from django.forms import ModelForm
from . import models

class UsuariosForm(ModelForm):
    class Meta:
        model=models.Usuarios
        fields='__all__'