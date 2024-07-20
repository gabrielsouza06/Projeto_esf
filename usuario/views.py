from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from .forms import PessoaForm
from .models import Pessoa
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
# Lista de Pessoas
class PessoaListView(ListView):
    model = Pessoa
    template_name = 'usuario/lista_pessoas.html'
    context_object_name = 'pessoas'


# Criação de Pessoa
class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'usuario/form_pessoa.html'
    success_url = reverse_lazy('usuarios:lista_pessoas')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('cpf', 'O CPF já está em uso como nome de usuário. Cadastre um CPF diferente.')
            return self.form_invalid(form)

# Edição de Pessoa
class PessoaUpdateView(LoginRequiredMixin, UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'usuario/form_pessoa.html'
    success_url = reverse_lazy('usuarios:lista_pessoas')
    login_url = 'login'

# Detalhe da Pessoa
class PessoaDetailView(LoginRequiredMixin, DetailView):
    model = Pessoa
    template_name = 'usuario/pessoa_detail.html'
    context_object_name = 'pessoa'
    login_url = 'login'  # URL para redirecionar se o usuário não estiver logado

# Exclusão de Pessoa
class PessoaDeleteView(LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'usuario/pessoa_confirm_delete.html'
    success_url = reverse_lazy('usuarios:lista_pessoas')
    login_url = 'login'  # URL para redirecionar se o usuário não estiver logado
