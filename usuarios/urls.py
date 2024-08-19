from django.urls import path
from . import views

urlpatterns = [
    path('usuario_list/', views.usuario_list, name='usuario_list'),
    path('usuarios/new/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:pk>/edit/', views.usuario_update, name='usuario_update'),
    path('usuarios/<int:pk>/delete/', views.usuario_delete, name='usuario_delete'),
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),

    path('register/', views.register, name='register'),

    path('', views.home, name='home'),

    # URLs para Profissional
    path('profissionais/', views.profissional_list, name='profissional_list'),
    path('profissionais/<int:pk>/', views.profissional_detail, name='profissional_detail'),
    path('profissionais/novo/', views.profissional_create, name='profissional_create'),
    path('profissionais/<int:pk>/editar/', views.profissional_update, name='profissional_update'),
    path('profissionais/<int:pk>/deletar/', views.profissional_delete, name='profissional_delete'),

    # URLs para Paciente
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('pacientes/<int:pk>/', views.paciente_detail, name='paciente_detail'),
    path('pacientes/novo/', views.paciente_create, name='paciente_create'),
    path('pacientes/<int:pk>/editar/', views.paciente_update, name='paciente_update'),
    path('pacientes/<int:pk>/deletar/', views.paciente_delete, name='paciente_delete'),
]
