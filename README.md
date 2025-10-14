# udemy-python-django-operacoes
Python/Django Operacoes APP do curso de Python em 6 horas

## Roteiro:

* django-admin startproject operacoes .

* python manage.py runserver

* pip install Pillow

* python manage.py migrate

* python manage.py createsuperuser

* Editar setings.py de operacoes e alterar:
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

* Criar o modulo de endereços: 

1) python manage.py startapp enderecos

2) Criar a classe Endereco no model de enderecos

3) Editar setings.py de operacoes em em INSTALLED_APPS adicionar enderecos

4) Editar admin.py em operacoes e adicionar admin.site.register(Endereco) e importar a classe com admin.site.register(Endereco) 

5) python manage.py makemigrations

6) python manage.py migrate

* Repetir os passos de 1 a 6 para criar os demais módulos