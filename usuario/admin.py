from django.contrib import admin
from .models import Pessoa, Paciente, Profissional

admin.site.register(Pessoa) 
admin.site.register(Paciente)  
admin.site.register(Profissional)
