from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dadad/', include('usuarios.urls')),
    path('consultas/', include('consultas.urls')),
    path('accounts/', include(urls)),
    path('estabelecimento/', include('estabelecimento.urls')),
    
]
