from django.urls import path
from .views import *


urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('cadastrar-cliente', CadastrarCliente.as_view(), name='cadastro-cliente'),
    path('cadastrar-usuario', Usuario.as_view(), name='usuario'),
    path('clientes', ListarCliente.as_view(), name='cliente'),
    path('deletar-cliente/<int:pk>/', DeletarCliente.as_view(), name='deletar-cliente'),
    path('editar-cliente/<int:pk>/', EditarCliente.as_view(), name='editar-cliente'),
    path('logout', Logout.as_view(), name='logout')
]
