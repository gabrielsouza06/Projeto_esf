from django import forms
from .models import Prontuario, Consulta

class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = [ 'status']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data_hora', 'status', 'profissional', 'paciente', 'estabelecimento', 'prontuario']
