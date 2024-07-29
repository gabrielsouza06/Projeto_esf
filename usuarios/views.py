from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from .models import Paciente, Profissional
from .forms import PacienteForm, ProfissionalForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    form_class = AuthenticationForm

    def get_success_url(self):
        if self.request.user.is_paciente:
            return reverse_lazy('paciente_home')
        elif self.request.user.is_profissional:
            return reverse_lazy('profissional_home')
        return super().get_success_url()

@login_required
def paciente_home(request):
    return render(request, 'paciente_home.html')

@login_required
def profissional_home(request):
    return render(request, 'profissional_home.html')


class ESFHomeView(TemplateView):
    template_name = 'home.html'

class PacienteListView(ListView):
    model = Paciente
    template_name = 'usuarios/paciente/paciente_list.html'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'usuarios/paciente/paciente_detail.html'

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'usuarios/paciente/paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'usuarios/paciente/paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'usuarios/paciente/paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')

class ProfissionalListView(ListView):
    model = Profissional
    template_name = 'usuarios/profissional/profissional_list.html'

class ProfissionalDetailView(DetailView):
    model = Profissional
    template_name = 'usuarios/profissional/profissional_detail.html'

class ProfissionalCreateView(CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'usuarios/profissional/profissional_form.html'
    success_url = reverse_lazy('profissional_list')

class ProfissionalUpdateView(UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'usuarios/profissional/profissional_form.html'
    success_url = reverse_lazy('profissional_list')

class ProfissionalDeleteView(DeleteView):
    model = Profissional
    template_name = 'usuarios/profissional/profissional_confirm_delete.html'
    success_url = reverse_lazy('profissional_list')
