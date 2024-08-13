from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente','profissional','estabelecimento','data_hora', 'status']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
