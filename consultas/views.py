from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConsultaForm
from .models import Consulta
from django.contrib.auth.decorators import login_required

@login_required
def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm()
    
    return render(request, 'consultas/agendar_consulta.html', {'form': form})

def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/listar_consultas.html', {'consultas': consultas})

@login_required
def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm(instance=consulta)
    
    return render(request, 'consultas/editar_consulta.html', {'form': form})

@login_required
def excluir_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('listar_consultas')
    return render(request, 'consultas/excluir_consulta.html', {'consulta': consulta})
