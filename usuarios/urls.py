from django.urls import path
from .views import (
    PacienteListView, PacienteDetailView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView,ProfissionalListView, ProfissionalDetailView, ProfissionalCreateView, ProfissionalUpdateView, ProfissionalDeleteView,
)

app_name = 'usuarios'

urlpatterns = [
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('pacientes/create/', PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/update/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/delete/', PacienteDeleteView.as_view(), name='paciente_delete'),
    path('profissionais/', ProfissionalListView.as_view(), name='profissional_list'),
    path('profissionais/<int:pk>/', ProfissionalDetailView.as_view(), name='profissional_detail'),
    path('profissionais/create/', ProfissionalCreateView.as_view(), name='profissional_create'),
    path('profissionais/<int:pk>/update/', ProfissionalUpdateView.as_view(), name='profissional_update'),
    path('profissionais/<int:pk>/delete/', ProfissionalDeleteView.as_view(), name='profissional_delete'),
]
