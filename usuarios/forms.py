from django import forms
from .models import Paciente, Profissional

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'
