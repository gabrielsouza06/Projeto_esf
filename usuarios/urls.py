from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("<int:usuario_id>/", views.detail, name="detail"),
    path("edit/<int:usuario_id>/", views.edit, name="edit"),
    path("del/<int:usuario_id>/", views.delete, name="delete"),
]
