from django.urls import path, include
from . import views

app_name='Comentarios'

urlpatterns = [
    path('Mostrar',views.Mostrar,name='Mostrar'),
    path('Comentar/<str:pk>',views.Comentar.as_view(), name='Comentar'),
]