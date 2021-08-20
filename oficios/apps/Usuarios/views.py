from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from . import models
# Create your views here.
@login_required
def Perfil(request):
    return render(request,'Usuarios/Perfil.html')

class BorrarPerfil(generic.DeleteView):
    model = models.Usuarios
    template_name = 'Usuarios/BorrarPerfil.html'
    success_url = reverse_lazy('logout')