from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from .models import Paciente, Profissional
from .forms import PacienteForm, ProfissionalForm

class ESFHomeView(TemplateView):
    template_name = 'home.html'

class PacienteListView(ListView):
    model = Paciente
    template_name = 'usuarios/paciente_list.html'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'usuarios/paciente_detail.html'

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'usuarios/paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'usuarios/paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'usuarios/paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')

class ProfissionalListView(ListView):
    model = Profissional
    template_name = 'usuarios/profissional_list.html'

class ProfissionalDetailView(DetailView):
    model = Profissional
    template_name = 'usuarios/profissional_detail.html'

class ProfissionalCreateView(CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'usuarios/profissional_form.html'
    success_url = reverse_lazy('profissional_list')

class ProfissionalUpdateView(UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'usuarios/profissional_form.html'
    success_url = reverse_lazy('profissional_list')

class ProfissionalDeleteView(DeleteView):
    model = Profissional
    template_name = 'usuarios/profissional_confirm_delete.html'
    success_url = reverse_lazy('profissional_list')
