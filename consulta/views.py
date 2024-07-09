from django.shortcuts import render
from django.http import HttpResponse

#lista consulta
def index(request):
    
    return render(request, 'consulta/lista.html', {})

#add consulta
def add(request):
    
    return HttpResponse('<h3>Aqui add!</h3>')

#deleta consulta
def delete(request, id_consulta):
    
    return HttpResponse('<h3>Aqui deleta!</h3>')

#edita consulta
def edit(request, id_consulta):
    
    return HttpResponse('<h3>Aqui edita!</h3>')