from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Prontuario, Consulta
from .forms import ProntuarioForm, ConsultaForm


def prontuario_list(request):
    prontuarios = Prontuario.objects.all()
    return render(request, 'prontuario_list.html', {'prontuarios': prontuarios})

def prontuario_detail(request, pk):
    prontuario = get_object_or_404(Prontuario, pk=pk)
    return render(request, 'prontuario_detail.html', {'prontuario': prontuario})

def prontuario_create(request):
    if request.method == "POST":
        form = ProntuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prontuario_list')
    else:
        form = ProntuarioForm()
    return render(request, 'prontuario_form.html', {'form': form})

def prontuario_update(request, pk):
    prontuario = get_object_or_404(Prontuario, pk=pk)
    if request.method == "POST":
        form = ProntuarioForm(request.POST, instance=prontuario)
        if form.is_valid():
            form.save()
            return redirect('prontuario_list')
    else:
        form = ProntuarioForm(instance=prontuario)
    return render(request, 'prontuario_form.html', {'form': form})

def prontuario_delete(request, pk):
    prontuario = get_object_or_404(Prontuario, pk=pk)
    if request.method == "POST":
        prontuario.delete()
        return redirect('prontuario_list')
    return render(request, 'prontuario_confirm_delete.html', {'prontuario': prontuario})

# Views para Consulta

def consulta_list(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/consulta_list.html', {'consultas': consultas})

def consulta_detail(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    return render(request, 'consultas/consulta_detail.html', {'consulta': consulta})

def consulta_create(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_list')
    else:
        form = ConsultaForm()
    return render(request, 'consultas/consulta_form.html', {'form': form})

def consulta_update(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == "POST":
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta_list')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'consultas/consulta_form.html', {'form': form})

def consulta_delete(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect('consulta_list')
    return render(request, 'consultas/consulta_confirm_delete.html', {'consulta': consulta})
