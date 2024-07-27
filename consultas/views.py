from django.shortcuts import render, redirect
from .forms import ConsultaForm

def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('esf_home')  # Substitua por uma URL de sucesso
    else:
        form = ConsultaForm()
    
    return render(request, 'consultas/agendar_consulta.html', {'form': form})

