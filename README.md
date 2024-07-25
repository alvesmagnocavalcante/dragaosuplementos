# Dragão Suplementos

Bem-vindo ao repositório do Dragão Suplementos, uma loja virtual para venda de suplementos alimentares construída com Django e Bootstrap.

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão Geral

O Dragão Suplementos é um projeto de e-commerce desenvolvido para a venda de suplementos alimentares. O projeto utiliza Django para o back-end e Bootstrap para o front-end, oferecendo uma experiência de usuário agradável e responsiva.

## Funcionalidades

- **Listagem de Produtos**: Exibe todos os produtos disponíveis com detalhes.
- **Detalhes do Produto**: Página dedicada para cada produto com descrição completa e imagem.
- **Pagamento Online**: Integração com Stripe para processamento seguro de pagamentos.
- **Contato via WhatsApp e Instagram**: Links diretos para redes sociais.
- **Layout Responsivo**: Design que se adapta a diferentes tamanhos de tela.
- **Personalização com Bootstrap**: Estilo visual coerente e personalizável com Bootstrap.

## Instalação

Siga as etapas abaixo para configurar o projeto localmente:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/draçao-suplementos.git
    cd draçao-suplementos
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o admin do Django:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Configuração

1. Configure as chaves do Stripe no seu arquivo `settings.py`:
    ```python
    STRIPE_PUBLIC_KEY = 'sua-chave-publica-do-stripe'
    STRIPE_SECRET_KEY = 'sua-chave-secreta-do-stripe'
    ```

2. Adicione as imagens e logo na pasta `static/images/`.

## Uso

- Acesse `http://127.0.0.1:8000/` no navegador para ver a loja online.
- Acesse `http://127.0.0.1:8000/admin/` para entrar no painel administrativo do Django.

## Estrutura do Projeto

```plaintext
draçao-suplementos/
├── dsuplementos/
│   ├── migrations/
│   ├── static/
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   ├── lista_produto.html
│   │   ├── detalhe_produto.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── draçao-suplementos/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
