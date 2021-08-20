from django.urls import path, include
from . import views

app_name='Zonas'

urlpatterns = [
	path('Listar/', views.ListarZonas.as_view(), name = "listar"),

]