from django.urls import path
from . import views

urlpatterns = [
    path('vacinas/', views.vacina_list, name='vacina_list'),
    path('vacinas/new/', views.vacina_create, name='vacina_create'),
    path('vacinas/<int:pk>/edit/', views.vacina_update, name='vacina_update'),
    path('vacinas/<int:pk>/delete/', views.vacina_delete, name='vacina_delete'),
    path('vacinas/<int:pk>/ajustar/', views.ajustar_quantidade_vacina, name='ajustar_quantidade_vacina'),
    path('remedios/', views.remedio_list, name='remedio_list'),
    path('remedios/new/', views.remedio_create, name='remedio_create'),
    path('remedios/<int:pk>/edit/', views.remedio_update, name='remedio_update'),
    path('remedios/<int:pk>/delete/', views.remedio_delete, name='remedio_delete'),
    path('remedios/<int:pk>/ajustar/', views.ajustar_quantidade, name='ajustar_quantidade'),
]
