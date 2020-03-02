from django.shortcuts import render, redirect
from django.views import View
from .models import Cliente
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.

class ListarCliente(View):

    def get(self, request):
        context = {}
        try: 
            clientes = Cliente.objects.all()
            context['clientes'] = list(clientes)
        except:
            context['clientes'] = []
        return render(request, 'cliente/listagem.html', context)

class CadastrarCliente(View):

    def get(self, request):
        return render(request, 'cliente/cadastrar-cliente.html')

    def post(self, request):
        print('entrou no cadastrar cliente')
        context = {}
        teste = False
        try:
            print(request.POST)
            print('dentro do try')
            novo_cliente = Cliente()           
            novo_cliente.nome = request.POST['nome']
            novo_cliente.telefone = request.POST['telefone']
            novo_cliente.endereco = request.POST['endereco']
            novo_cliente.numero = request.POST['numero']
            novo_cliente.cidade = request.POST['cidade']
            novo_cliente.estado = request.POST['estado']
            novo_cliente.pais = request.POST['pais']
            novo_cliente.cep = request.POST['cep']
            novo_cliente.save()
            teste = True
            context['mensagem'] = "Cliente Cadastrado com sucesso."
            print('try encerrado')
        except:
            teste = False
            print('entrou no except')
            context['mensagem'] = "Cliente não cadastrado."
            
        context['status'] = teste
        return render(request, 'cliente/listagem.html', context)

class DeletarCliente(View):

    def post(self, request):
        print(request.POST['id'])
        context = { }
        teste = False
        try:
            cliente = Cliente.objects.get(id=request.POST['id'])
            print(cliente.nome)
            cliente.delete()
            context['mensagem'] = "Cliente removido com sucesso."
            teste = True
        except:
            context['mensagem'] = "Não foi possível remover o cliente, tente novamente."
            teste = False
        context['status'] = teste
        return JsonResponse(context)

class EditarCliente(View):

    def post(self, request):

        return ''       

class Login(View):

    def get(self, request):
        return render(request, 'login/signin.html')

    def post(self, request):
        return ''

    def validadorDeLogin(self):
        return ''

class Usuario(View):

    def get(self, request):
        return render(request, 'usuario/cadastrar-usuario.html')

    def post(self, request):
        context = {}
        teste = False
        try:
            usuario = User()
            usuario.username = request.POST['nome']
            usuario.email = request.POST['email']
            usuario.password = request.POST['senha']
            usuario.save()
            teste = True
            context["mensagem"] = "Usuário Cadastrado com sucesso."
        except:
            teste = False
            context["mensagem"] = "Houve algum problema, tente novamente."
        # terminar com a mensagem e com o redirecionamento correto.
        
        context["status"] = teste
        return JsonResponse(context)

    
        