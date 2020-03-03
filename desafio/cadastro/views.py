from django.shortcuts import render, redirect
from django.views import View
from .models import Cliente
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

class ListarCliente(View):
    
    def get(self, request):
        context = {}
        if request.user.is_anonymous:
            return redirect('login')
        else:
            try: 
                clientes = Cliente.objects.all()
                context['clientes'] = list(clientes)
            except:
                context['clientes'] = []
            return render(request, 'cliente/listagem.html', context)


class CadastrarCliente(View):
    
    def get(self, request):
        if request.user.is_anonymous:
            return redirect('login')
        else:
            return render(request, 'cliente/cadastrar-cliente.html')

    def post(self, request):
        if request.user.is_anonymous:
            return redirect('login')
        else:
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
                messages.success(request, "Cliente cadastrado com sucesso.")
                return redirect('cliente')
            except:
                messages.error(request, "Algo deu errado. Tente novamente")
                return redirect('cadastro-cliente')


class DeletarCliente(View):
    
    def post(self, request, pk):
        if request.user.is_anonymous:
            return redirect('login')
        else:
            try:
                cliente = Cliente.objects.get(id=pk)
                print(cliente.nome)
                cliente.delete()
                messages.success(request, "Cliente removido com sucesso.")
            except:
                messages.error(request, "Algo deu errado. Tente novamente")
            
            return redirect('cliente')


class EditarCliente(View):

    def get(self, request, pk):
        if request.user.is_anonymous:
            return redirect('login')
        else:
            return render(request, 'cliente/editar-cliente.html', {'id' : pk})

    def post(self, request, pk):
        if request.user.is_anonymous:
            return redirect('login')
        else:
            try:
                cliente = Cliente.objects.get(id=pk)
                cliente.nome = request.POST.get('nome')
                cliente.telefone = request.POST.get('telefone')
                cliente.endereco = request.POST.get('endereco')
                cliente.numero = request.POST.get('numero')
                cliente.cidade = request.POST.get('cidade')
                cliente.estado = request.POST.get('estado')
                cliente.pais = request.POST.get('pais')
                cliente.cep = request.POST.get('cep')
                cliente.save()
                messages.success(request, "Cliente editado com sucesso.")
            except:
                messages.error(request, "Algo deu errado. Tente novamente")
                
            return redirect('cliente')

class Login(View):

    def get(self, request):
        return render(request, 'login/signin.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('senha')
        usernamelog = User.objects.get(email=email)
        print(usernamelog)
        user = authenticate(request, username=usernamelog, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('cliente')
        else:
            messages.error(request, "Email ou senha inválidos. Favor tentar novamente.")
        return redirect('login')


class Logout(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')


class Usuario(View):

    def get(self, request):
        return render(request, 'usuario/cadastrar-usuario.html')

    def post(self, request):
             
        try:
            user = User.objects.create_user(request.POST.get('nome'), request.POST.get('email').lower(), request.POST.get('senha'))
            messages.success(request, "Usuário Cadastrado com sucesso.")
            return redirect('login')
        except:
            messages.error(request, "Houve algum problema, tente novamente.")
        return redirect('usuario')
        
class UserManager(BaseUserManager):

    def create_user(self, nome, email, password=None):
        if not email:
            raise ValueError("Os usuários devem ter um endereço de email")
        
        user = self.model(username=nome, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    
        