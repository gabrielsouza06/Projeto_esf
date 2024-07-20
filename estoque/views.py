from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacina, Remedio
from .forms import VacinaForm, RemedioForm, AjustarQuantidadeForm

def vacina_list(request):
    vacinas = Vacina.objects.all()
    return render(request, 'estoque/vacina_list.html', {'vacinas': vacinas})

def remedio_list(request):
    remedios = Remedio.objects.all()
    return render(request, 'estoque/remedio_list.html', {'remedios': remedios})

def vacina_create(request):
    if request.method == 'POST':
        form = VacinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacina_list')
    else:
        form = VacinaForm()
    return render(request, 'estoque/vacina_form.html', {'form': form})

def remedio_create(request):
    if request.method == 'POST':
        form = RemedioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('remedio_list')
    else:
        form = RemedioForm()
    return render(request, 'estoque/remedio_form.html', {'form': form})

def vacina_update(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == 'POST':
        form = VacinaForm(request.POST, instance=vacina)
        if form.is_valid():
            form.save()
            return redirect('vacina_list')
    else:
        form = VacinaForm(instance=vacina)
    return render(request, 'estoque/vacina_form.html', {'form': form})

def remedio_update(request, pk):
    remedio = get_object_or_404(Remedio, pk=pk)
    if request.method == 'POST':
        form = RemedioForm(request.POST, instance=remedio)
        if form.is_valid():
            form.save()
            return redirect('remedio_list')
    else:
        form = RemedioForm(instance=remedio)
    return render(request, 'estoque/remedio_form.html', {'form': form})

def vacina_delete(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    if request.method == 'POST':
        vacina.delete()
        return redirect('vacina_list')
    return render(request, 'estoque/vacina_confirm_delete.html', {'vacina': vacina})

def remedio_delete(request, pk):
    remedio = get_object_or_404(Remedio, pk=pk)
    if request.method == 'POST':
        remedio.delete()
        return redirect('remedio_list')
    return render(request, 'estoque/remedio_confirm_delete.html', {'remedio': remedio})

def ajustar_quantidade(request, pk):
    remedio = get_object_or_404(Remedio, pk=pk)
    
    if request.method == 'POST':
        form = AjustarQuantidadeForm(request.POST)
        if form.is_valid():
            ajuste = form.cleaned_data['ajuste']
            quantidade = form.cleaned_data['quantidade']
            
            if ajuste == '+':
                remedio.quantidade += quantidade
            elif ajuste == '-' and remedio.quantidade >= quantidade:
                remedio.quantidade -= quantidade
            else:
                form.add_error('quantidade', 'Quantidade a subtrair é maior que a quantidade disponível.')

            remedio.save()
            return redirect('remedio_list')
    else:
        form = AjustarQuantidadeForm()
    
    return render(request, 'estoque/remedio_ajustar_quantidade.html', {'form': form, 'remedio': remedio})

def ajustar_quantidade_vacina(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)
    
    if request.method == 'POST':
        form = AjustarQuantidadeForm(request.POST)
        if form.is_valid():
            ajuste = form.cleaned_data['ajuste']
            quantidade = form.cleaned_data['quantidade']
            
            if ajuste == '+':
                vacina.quantidade += quantidade
            elif ajuste == '-' and vacina.quantidade >= quantidade:
                vacina.quantidade -= quantidade
            else:
                form.add_error('quantidade', 'Quantidade a subtrair é maior que a quantidade disponível.')

            vacina.save()
            return redirect('vacina_list')
    else:
        form = AjustarQuantidadeForm()
    
    return render(request, 'estoque/vacina_ajustar_quantidade.html', {'form': form, 'vacina': vacina})