from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('cadastrar-cliente', login_required(CadastrarCliente.as_view()), name='cadastro-cliente'),
    path('cadastrar-usuario', Usuario.as_view(), name='usuario'),
    path('clientes', login_required(ListarCliente.as_view()), name='cliente'),
    path('deletar-cliente', login_required(DeletarCliente.as_view()), name='deletar-cliente'),
    path('editar-cliente', login_required(EditarCliente.as_view()), name="editar-cliente"),
    path('logout', Logout.as_view(), name='logout')
]
