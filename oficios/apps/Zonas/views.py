from django.views.generic.edit import CreateView 
from django.shortcuts import render
from ..Zonas.models import Zonas
from django.urls import reverse_lazy
from ..utils.funciones import PermisosMixin,PasajeMixin
from django.views.generic.list import ListView
# Create your views here.

class ListarZonas(ListView):
	model = Zonas
	template_name = 'Zonas/listar.html'
     