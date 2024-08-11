from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm
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
