from django.urls import path
from . import views

urlpatterns = [
    path('agendar/', views.agendar_consulta, name='agendar_consulta'),
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('consultas/editar/<int:pk>/', views.editar_consulta, name='editar_consulta'),
    path('consultas/excluir/<int:pk>/', views.excluir_consulta, name='excluir_consulta'),
]
