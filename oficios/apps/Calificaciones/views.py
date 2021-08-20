from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from ..utils.funciones import PermisosMixin,PasajeMixin
from .forms import CalificacionesForm
from ..Trabajadores.models import Trabajadores
from .models import Calificaciones
from django.db.models import Avg

class Calificar(LoginRequiredMixin,PermisosMixin,PasajeMixin,CreateView):
    model=Calificaciones
    form_class=CalificacionesForm
    template_name='Calificaciones/Calificar.html'
    rol='stalker'
    campos=['perfil','objeto']

    def tratar_perfil(self,perfil,form,instancia,objeto):
        form.save(commit=True)
        instancia.stalker.add(perfil)
        avg=Calificaciones.objects.filter(trabajador=objeto).aggregate(Avg('calificacion'))
        objeto.promedio = avg['calificacion__avg']
        objeto.save()