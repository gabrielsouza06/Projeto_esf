from django import forms
from .models import Vacina, Remedio

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'descricao', 'quantidade']

class RemedioForm(forms.ModelForm):
    class Meta:
        model = Remedio
        fields = ['nome', 'descricao', 'quantidade']


from django import forms

class AjustarQuantidadeForm(forms.Form):
    OPCAO_AJUSTE = [
        ('+', 'Adicionar'),
        ('-', 'Subtrair'),
    ]
    ajuste = forms.ChoiceField(choices=OPCAO_AJUSTE, label='Operação')
    quantidade = forms.IntegerField(min_value=1, label='Quantidade')

