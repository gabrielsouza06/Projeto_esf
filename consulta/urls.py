
from django.urls import path
from consulta import views

urlpatterns = [
    path('', views.index, name='lista-consulta'),
    path('add/', views.add, name='add-consulta'),
    path('delete/<int:id_consulta>', views.delete, name='apaga-consulta'),
    path('edit/<int:id_consulta>', views.edit, name='edita-consulta')
]