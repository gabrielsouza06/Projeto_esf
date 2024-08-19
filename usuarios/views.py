from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Profissional, Paciente
from .forms import UsuarioForm, ProfissionalForm, PacienteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from projeto_esf3.views import create_groups


def home(request):
    create_groups()
    return render(request, 'home.html')

@login_required
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listaTodos.html', {'usuarios': usuarios})

@login_required
def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuarios/usuario_detail.html', {'usuario': usuario})

@login_required
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Adiciona o usuário ao grupo "Profissional" automaticamente
            group, created = Group.objects.get_or_create(name='Profissional')
            user.groups.add(group)

            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    
    return render(request, 'usuarios/form.html', {'form': form})

@login_required
def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/form.html', {'form': form})

@login_required
def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})



def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # Adiciona o usuário ao grupo "Paciente" automaticamente
            group, created = Group.objects.get_or_create(name='Paciente')
            user.groups.add(group)

            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UsuarioForm()
    
    return render(request, 'usuarios/register.html', {'form': form})


#CRUD de Proficional

@login_required
def profissional_list(request):
    profissionais = Profissional.objects.all()
    return render(request, 'profissionais/lista_profissionais.html', {'profissionais': profissionais})

@login_required
def profissional_detail(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)
    return render(request, 'profissionais/profissional_detail.html', {'profissional': profissional})

@login_required
def profissional_create(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            profissional = form.save()

            # Adiciona o profissional ao grupo "Profissional" automaticamente
            group, created = Group.objects.get_or_create(name='Profissional')
            profissional.groups.add(group)

            return redirect('profissional_list')
    else:
        form = ProfissionalForm()
    
    return render(request, 'profissionais/form.html', {'form': form})

@login_required
def profissional_update(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)
    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('profissional_list')
    else:
        form = ProfissionalForm(instance=profissional)
    return render(request, 'profissionais/form.html', {'form': form})

@login_required
def profissional_delete(request, pk):
    profissional = get_object_or_404(Profissional, pk=pk)
    if request.method == 'POST':
        profissional.delete()
        return redirect('profissional_list')
    return render(request, 'profissionais/profissional_confirm_delete.html', {'profissional': profissional})


#CRUD de Paciente 

@login_required
def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista_pacientes.html', {'pacientes': pacientes})

@login_required
def paciente_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'pacientes/paciente_detail.html', {'paciente': paciente})


def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save()

            # Adiciona o paciente ao grupo "Paciente" automaticamente
            group, created = Group.objects.get_or_create(name='Paciente')
            paciente.groups.add(group)

            return redirect('paciente_list')
    else:
        form = PacienteForm()
    
    return render(request, 'pacientes/paciente_form.html', {'form': form})

@login_required
def paciente_update(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/paciente_form.html', {'form': form})

@login_required
def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_list')
    return render(request, 'pacientes/paciente_confirm_delete.html', {'paciente': paciente})
