from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_page_view, home_view

app_name = 'login'

urlpatterns = [
    path('', home_view, name='home'),  # Página inicial que pode ser acessada sem login
    path('user_page/', user_page_view, name='user_page'),  
]
