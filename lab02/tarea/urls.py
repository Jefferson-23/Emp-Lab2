from django.urls import path

from . import views

app_name = 'tarea'

urlpatterns = [
    path('', views.formulario_ope, name='formulario_ope'),
    path('calcular', views.calcular, name='calcular'),
]
