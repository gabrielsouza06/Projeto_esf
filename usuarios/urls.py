from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuario_list, name='usuario_list'),
    path('usuarios/new/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:pk>/edit/', views.usuario_update, name='usuario_update'),
    path('usuarios/<int:pk>/delete/', views.usuario_delete, name='usuario_delete'),
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),
]
