# udemy-python-django-operacoes
Python/Django Operacoes APP do curso de Python em 6 horas

## Comando para execução da aplicação:

* python manage.py runserver

## Roteiro para criação do projeto:

* django-admin startproject operacoes .

* pip install Pillow

* python manage.py migrate

* python manage.py createsuperuser

* Editar setings.py de operacoes e alterar:
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

* Criar o modulo de endereços: 

1) python manage.py startapp enderecos

2) Criar a classe Endereco no model de enderecos

3) Editar settings.py de operacoes em INSTALLED_APPS adicionar enderecos

4) Editar admin.py de operacoes e adicionar: admin.site.register(Endereco) e importar a classe com admin.site.register(Endereco) 

5) python manage.py makemigrations

6) python manage.py migrate

* Repetir os passos de 1 a 6 para criar os demais módulos

7) Editar settings.py de operacoes e adicionar: MEDIA_URL = '/media/'

8) Editar settings.py de operacoes e adicionar: MEDIA_ROOT = 'media'

9) Editar urls.py de operacoes em urlpatterns adicionar: + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

10) Editar settings.py de operacoes e adicionar: DATE_FORMAT = 'd/m/Y'

11) Editar settings.py de operacoes e adicionar: DATE_INPUT_FORMATS = ('%d/%m/%Y',)

12) Editar settings.py de operacoes e alterar USE_I18N = False

13) Classes com nomes com caracteres especiais podem usar um atributo META para informar a exibição correta

14) Classes como admin de diligencias podem conter uma classe Admin que configura exibição da listagem e filtros de busca 