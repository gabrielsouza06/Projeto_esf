from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from django.contrib.auth.models import User

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    if request.method == 'POST':
        # Get form data
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')

        pessoa = Pessoa.objects.create(
            nome=nome,
            sobrenome=sobrenome,
            senha=senha,
            email=email
        )

    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "editar_pessoa.html", {"pessoa": pessoa})
    return redirect(home)


def update(request, id):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome
    pessoa.sobrenome = sobrenome
    pessoa.email = email
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

def login(request):
    return render(request, 'login.html')