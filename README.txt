# SHOPSTORE

## Escopo
Sistema para cadastro, listagem, detalhes, edição e exclusão de:
	- administradores e usuários, para login e acessos especiais;
	- produtos;
	- bancos, contas, fatura, produtos da fatura e faturamento;
	- categoria de despesa, tipo de despesa e pagamento;
	- fornecedor/cliente
	
utilizando o framework Django 3.2.5 e a linguagem de programação Python 3.9.5


# Funcionalidades

* Administrador/Usuário:
	- Cadastro:
    		nome
		email
		senha
	- com o cadastro concluído, será enviado link no email informado, para confirmar o cadastro;
	- o link direcionará para um formulário de conclusão de cadastro;
	- concluído o cadastro, o usuário será automaticamente logado.
* login (email e senha):
	- link para recuperação de senha.
	- formulário para informar email cadastrado para envio do link de recuperação de senha.
	- o link enviado redicionará para o formulário de renovação de senha.
* logout:
	- tela para confirmar logout.

* perfil de usuários:
	- tela para exibir
	- formulário para editar
	- tela para confirmar exclusão

* contato
	- formuláro para envio de mensagens ao administrador do framework;


## Instalando


### Criar ambiente virtual

```
pip install virtualenv 
virtualenv .venv_shopstore
```


### Ativar ambiente virtual

```
.\.venv_shopstore/Scripts/Activate
```


### Clonar o projeto

```
git clone 
```


### Acessar a pasta do projeto

```
cd shopstore
```


### Instalar dependências

```
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```


### Aplicar migrações

```
python manage.py migrate
```


### Criar super usuário

```
python manage.py createsuperuser
```

obs.: o email será utilizado como username para login


### Rodar o projeto

```
python manage.py runserver
```













========================= ATUALIZAÇÕES
profile - user
inserir botão google na tela cadastro
tela login google
