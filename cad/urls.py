from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, delete, pagina1
from django.conf import settings

urlpatterns = [
    path('', pagina1, name='pagina1'),
    path('home/', home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),

]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()