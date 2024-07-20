from django.urls import path
from .views import PessoaListView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView, PessoaDetailView

app_name = 'usuarios'

urlpatterns = [
    path('', PessoaListView.as_view(), name='lista_pessoas'),
    path('add/', PessoaCreateView.as_view(template_name='Usuario/form_pessoa.html'), name='nova_pessoa'),
    path('edit/<int:pk>/', PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('delete/<int:pk>/', PessoaDeleteView.as_view(), name='excluir_pessoa'),
    path('detalhes/<int:pk>/', PessoaDetailView.as_view(), name='detalhes_pessoa'),
]
