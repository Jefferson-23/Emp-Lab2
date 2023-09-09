from django.urls import path

from . import views

app_name = 'cilindro'

urlpatterns = [
    path('', views.formulario_cili, name='formulario_cili'),
    path('calcular', views.calcular, name='calcular'),
]