from django.urls import path
from . import views

app_name='Calificaciones'

urlpatterns = [
    path('Calificar/<str:pk>/', views.Calificar.as_view(), name = 'Calificar'),
]