# 🐍 Django Operações App

Aplicação desenvolvida durante o curso **Python em 6 horas (Udemy)**:  
https://www.udemy.com/course/aprenda-python-3-em-6h/

Este projeto demonstra a criação de um sistema Django completo com múltiplos módulos e upload de imagens.


## 🧩 Comandos a executar na primeira vez após baixar o repositório

Ao clonar este projeto em uma nova máquina, é necessário recriar o ambiente virtual e instalar as dependências antes de executar a aplicação.  
Siga os comandos abaixo (para sistemas Linux ou macOS):

```bash
# 1️⃣ Criar o ambiente virtual
python3 -m venv .venv

# 2️⃣ Ativar o ambiente virtual
source .venv/bin/activate

# 3️⃣ Atualizar o gerenciador de pacotes
python -m pip install --upgrade pip

# 4️⃣ Instalar as dependências principais
pip install django pillow

# 5️⃣ Aplicar as migrações iniciais do banco de dados
python manage.py migrate

# 6️⃣ Criar o usuário administrador (siga as instruções interativas)
python manage.py createsuperuser

# 7️⃣ Iniciar o servidor de desenvolvimento
python manage.py runserver
```

Após isso, acesse a aplicação em:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
E o painel administrativo em:  
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)



---

## ⚙️ Configuração do ambiente

Você pode criar o ambiente virtual (venv) de **duas formas**:

### 🔹 Opção 1 – Pelo PyCharm
- Crie um novo projeto e em **"Interpreter Type"** escolha **"Project venv"** ao criar o projeto.

### 🔹 Opção 2 – Via terminal
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Linux/Mac)
source venv/bin/activate

# No Windows
venv\Scripts\activate

# Instalar dependências

```



---

## 🚀 Criação do projeto

```bash
pip install django
django-admin startproject operacoes .
pip install django Pillow
python manage.py migrate
python manage.py createsuperuser
```

> 💡 **Pillow** é usado para lidar com imagens (upload e manipulação).

Editar `operacoes/settings.py`:

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

---

## 🧩 Criação do módulo de endereços

```bash
python manage.py startapp enderecos
```

1. Criar a classe `Endereco` no `models.py` do app.  
2. Registrar a aplicação no `settings.py` (`INSTALLED_APPS`).  
3. Editar `admin.py` e adicionar:
   ```python
   from .models import Endereco
   admin.site.register(Endereco)
   ```
4. Criar e aplicar migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

> 🔁 Repita esses passos para criar outros módulos do projeto.

---

## 🗂️ Configurações adicionais

Editar `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

DATE_FORMAT = 'd/m/Y'
DATE_INPUT_FORMATS = ('%d/%m/%Y',)
USE_I18N = False
```

Editar `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧠 Dicas

- Use `class Meta:` para nomes com caracteres especiais.  
- No `admin`, crie classes `ModelAdmin` para personalizar listagem e filtros.

---

## ▶️ Executar o projeto

```bash
python manage.py runserver
```

Acesse em: **http://127.0.0.1:8000/admin/**

Faça login com usuario = **'usuario'** e senha = **'senha'**
