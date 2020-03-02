from django.urls import path
from .views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('cadastrar-cliente', CadastrarCliente.as_view(), name='cadastro-cliente'),
    path('cadastrar-usuario', Usuario.as_view(), name='usuario'),
    path('clientes', ListarCliente.as_view(), name='cliente'),
    path('deletar-cliente', DeletarCliente.as_view(), name='deletar-cliente')
]
