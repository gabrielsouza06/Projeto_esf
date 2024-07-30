from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm

def index(request):

    usuarios = Usuario.objects.all()

    return render(request, "usuarios/listaTodos.html", {})

def add(request):

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpRedirect("/usuarios/")

    else:
        form = UsuarioForm()

    contexto = {
        'form': form
    }

    return render(request, "usuarios/form.html", contexto)

def detail(request, usuario_id):
    pass

def edit(request, usuario_id):
    pass

def delete(request, usuario_id):
    pass