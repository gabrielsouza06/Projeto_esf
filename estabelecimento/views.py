from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Estabelecimento
from .forms import EstabelecimentoForm
from django.contrib.auth.decorators import login_required

@login_required
def estabelecimento_list(request):
    estabelecimentos = Estabelecimento.objects.all()
    return render(request, 'estabelecimento/estabelecimento_list.html', {'estabelecimentos': estabelecimentos})

@login_required
def estabelecimento_detail(request, pk):
    estabelecimento = get_object_or_404(Estabelecimento, pk=pk)
    return render(request, 'estabelecimento/estabelecimento_detail.html', {'estabelecimento': estabelecimento})

@login_required
def estabelecimento_create(request):
    if request.method == "POST":
        form = EstabelecimentoForm(request.POST)
        if form.is_valid():
            estabelecimento = form.save()
            return redirect('estabelecimento_detail', pk=estabelecimento.pk)
    else:
        form = EstabelecimentoForm()
    return render(request, 'estabelecimento/estabelecimento_form.html', {'form': form})

@login_required
def estabelecimento_update(request, pk):
    estabelecimento = get_object_or_404(Estabelecimento, pk=pk)
    if request.method == "POST":
        form = EstabelecimentoForm(request.POST, instance=estabelecimento)
        if form.is_valid():
            estabelecimento = form.save()
            return redirect('estabelecimento_detail', pk=estabelecimento.pk)
    else:
        form = EstabelecimentoForm(instance=estabelecimento)
    return render(request, 'estabelecimento/estabelecimento_form.html', {'form': form})

@login_required
def estabelecimento_delete(request, pk):
    estabelecimento = get_object_or_404(Estabelecimento, pk=pk)
    if request.method == "POST":
        estabelecimento.delete()
        return redirect('estabelecimento_list')
    return render(request, 'estabelecimento/estabelecimento_confirm_delete.html', {'estabelecimento': estabelecimento})
