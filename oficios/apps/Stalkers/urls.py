from django.urls import path, include
from . import views

app_name='Stalkers'

urlpatterns = [
    path('Registro',views.Registro.as_view(),name='registro'),
    path('EditarPerfil/<str:pk>',views.EditarPerfil.as_view(),name='editarPerfil'),
]