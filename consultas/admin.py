from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data_hora', 'status')
    search_fields = ('status',)
    list_filter = ('status',)
