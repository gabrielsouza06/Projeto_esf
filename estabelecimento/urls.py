from django.urls import path
from . import views

urlpatterns = [
    path('', views.estabelecimento_list, name='estabelecimento_list'),
    path('<int:pk>/', views.estabelecimento_detail, name='estabelecimento_detail'),
    path('new/', views.estabelecimento_create, name='estabelecimento_create'),
    path('<int:pk>/edit/', views.estabelecimento_update, name='estabelecimento_update'),
    path('<int:pk>/delete/', views.estabelecimento_delete, name='estabelecimento_delete'),
]
