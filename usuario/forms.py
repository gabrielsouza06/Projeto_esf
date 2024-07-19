from django import forms
from usuario.models import Pessoa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            'nome_completo',
            'rua', 'bairro', 'numero', 'cidade', 
            'uf', 'rg', 'cpf', 'nome_mae', 'nome_pai'
        ]

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf.isdigit():
            raise forms.ValidationError("CPF deve conter apenas números.")
        
        # Verificar se o CPF já existe, exceto para o próprio registro em edição
        if Pessoa.objects.filter(cpf=cpf).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("CPF já cadastrado.")
        
        return cpf

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('cpf')
        user.set_unusable_password()  # Define a senha como não utilizável
        if commit:
            user.save()
        return user
