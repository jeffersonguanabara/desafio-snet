# desafio-snet

## Instalação

### Donwload do codigo

  git clone https://github.com/jeffersonguanabara/desafio-snet.git

### criando uma virtualenv

  Windows(powershell) ou Linux:
    * pip3 install virtualenv
    * virtualenv "nome-da-env"
    
### ativando a virtualenv
  
  Windows:
    * caminho do diretorio> . .\"nome-da-env"\Scripts\activate
  Linux:
    * caminho-do-diretorio$ . "nome-da-env"/bin/activate
                  ou
      caminho-do-diretorio$ source "nome-da-env"/bin/activate
      
### acessando a pasta do projeto django

    cd desagio-snet
    
### instalando as bibliotecas do projeto

    pip install -r requirements.txt
    
### acessando a pasta desafio, fazendo cofigurações do banco de dados:

   no arquivo settings.py, dentro da pasta desafio, procure pelo termo DATABASE, e configure o banco de acordo com as configurações em sua máquina:
   
   'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome-do-seu-banco',
        'USER': 'seu-usuario',
        'PASSWORD': 'sua-senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
    
### criando a base de dados

    acesse a pasta desafio e execute o comando:
      * python manage.py migrate
      
### execute o servidor

    python manage.py runserver 
    
## Execução do Sistema Web

    Com o servidor iniciado, abra seu navegador preferido e acesse o endereço: 127.0.0.1:8000. Assim a aplicação poderá ser executada.

### Login
    
    A nível de informação, infelizmente não consegui completar o desafio de autenticar usuário usando o Facebook, então será necessário cadastrar um usuário acessa no link cadastrar na página de login. Acessando assim a página de cadastro de usuário.    
    
    Na página de cadastro do usuário preencha os campos de nome, email e senha. Após clique em salva e você será redirecionado a página de login.
    
    O login dar-se-á passando o email e senha do usuário cadastrado. Podendo assim acessar as páginas internas do sistema.
    Após preencher os campos do formulário de login, clique em entrar e o sistemas se responsabilizará em autenticar o usuário.
    Caso o usuário não esteja cadastrado ou o sistema por um acaso não o encontre, o sistema deverá retornar a página de login para uma nova tentativa ou o cadastro do usuário.
    
### Listagem de Clientes

    Nessa página temos um botão para cadastro de novos clientes, e abaixo uma tabela que mostrará todos os clientes cadastrados.
    
    Ao clicar no botão "Novo Cliente", o sistema redirecionará o usuário a página de cadastrar novo cliente. Preencha todos os campos.
    Ao preencher o campo de CEP e com um "tab" do teclado, o sistema buscará as informações de alguns campos do formulário para preenchimento automático. Ao fim do preenchimento do formulário o sistema fará a busca no mapa ao lado e mostrará a localização informada do endereço no formulário.
    Após verificar se tudo ocorreu bem, basta clicar em salvar e o sistema retornará a listagem de cliente, mostrando o usuário recém cadastrado.
    Na tabela o usuário poderá fazer as ações de editar os clientes cadastrados e excluílos.
    Para editar cliente, clique no botão de editar na linha referente os cliente, indo assim a página de editar o cliente. Preencha todas as informações do formulário e clique em salvar.
    Para excluir cliente basta clicar sobre o botão excluir, e o sistema solicitará confirmação da operação, confirme, e então o sistema removerá o cliente da base de dados.
    
### Logout

    Na barra de navegação podemos visualizar o usuário logado e um botão "Sair", que ao ser clicado encerrará a sessão e retornará a página de login.
    

    Escrito por Jefferson Guanabara.

    
    
      

   
   
    

    

