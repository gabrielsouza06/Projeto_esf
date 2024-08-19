from django.urls import path
from . import views

urlpatterns = [
    # URLs para Prontuario
    path('prontuarios/', views.prontuario_list, name='prontuario_list'),
    path('prontuarios/<int:pk>/', views.prontuario_detail, name='prontuario_detail'),
    path('prontuarios/new/', views.prontuario_create, name='prontuario_create'),
    path('prontuarios/<int:pk>/edit/', views.prontuario_update, name='prontuario_update'),
    path('prontuarios/<int:pk>/delete/', views.prontuario_delete, name='prontuario_delete'),

    # URLs para Consulta
    path('consultas/', views.consulta_list, name='consulta_list'),
    path('consultas/<int:pk>/', views.consulta_detail, name='consulta_detail'),
    path('consultas/new/', views.consulta_create, name='consulta_create'),
    path('consultas/<int:pk>/edit/', views.consulta_update, name='consulta_update'),
    path('consultas/<int:pk>/delete/', views.consulta_delete, name='consulta_delete'),
]
