# Categorizador de E-mails com IA

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3.3-000000?logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white)

## Sumário

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Como funciona](#como-funciona)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Como executar](#como-executar)
- [Variáveis de ambiente](#variáveis-de-ambiente)
- [Rotas / Endpoints](#rotas--endpoints)
- [Autor](#autor)

## Sobre

O categorizador de e-mails com IA é uma ferramenta web simples e eficiente para criar respostas automáticas conforme a categoria do e-mail. Usando Inteligência Artificial (OpenAI `gpt-4o-mini`), a aplicação classifica o e-mail em **Produtivo** ou **Improdutivo** e gera uma resposta automática sugerida, podendo inclusive automatizar o envio dessa resposta via integração com n8n.

## Funcionalidades

- Classificação de e-mails colados diretamente em um formulário de texto.
- Classificação de e-mails enviados como arquivo `.pdf` ou `.txt`.
- Geração automática de uma resposta sugerida, de acordo com a categoria identificada.
- API (`/n8n`) para integrar a classificação/resposta a um fluxo de automação de envio de e-mail.

## Como funciona

1. O usuário envia o conteúdo do e-mail (texto colado ou arquivo `.pdf`/`.txt`).
2. `classify_email` ([project/classifier.py](project/classifier.py)) chama o modelo `gpt-4o-mini` para classificar o texto em `Produtivo` ou `Improdutivo`. Se a resposta do modelo não for uma dessas duas categorias, a classificação é rejeitada e a aplicação retorna erro.
3. `generate_response` ([project/classifier.py](project/classifier.py)) chama novamente o `gpt-4o-mini` para gerar uma resposta automática, curta e objetiva, de acordo com a categoria.
4. Para arquivos `.pdf`, o texto é extraído antes com `extrair_pdf` (via `pypdf`).
5. O resultado (categoria + resposta sugerida) é exibido na página ou, no caso da rota `/n8n`, retornado como JSON para ser usado por uma automação de envio de e-mail.

## Estrutura do projeto

```
categorizador-email/
├── Dockerfile              # imagem da aplicação (python:3.12-slim)
├── docker-compose.yaml     # serviços "web" (Flask) e "n8n" (automação de envio)
├── example.env             # modelo de variáveis de ambiente
├── requirements.txt        # dependências Python
└── project/
    ├── app.py              # rotas Flask (/, /upload, /n8n)
    ├── classifier.py       # classificação, geração de resposta e extração de PDF via OpenAI
    ├── static/              # favicon e logo
    └── templates/
        └── index.html      # página web (formulário de texto/upload)
```

## Tecnologias utilizadas

#### Back-end
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="100" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original-wordmark.svg" width="100"/>

#### IA
OpenAI - GPT-4o-MINI

#### Front-end
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-plain-wordmark.svg" width="100"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bootstrap/bootstrap-original-wordmark.svg" width="100"/>

#### Envio de E-mail
N8N - Automatizando o envio de e-mail <p>
Email para testes: thallesapi@gmail.com

#### Outras bibliotecas
- `pypdf` — extração de texto de arquivos `.pdf`
- `python-dotenv` — carregamento da chave da OpenAI a partir do `.env`

## Pré-requisitos

- Python **3.12** ou superior — **ou** Docker + Docker Compose.
- Uma chave de API da OpenAI.

## Como executar

### Localmente

1. Clone o repositório.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Crie um arquivo `.env` **na raiz do projeto** com a chave da OpenAI, seguindo o exemplo de [example.env](example.env):
   ```
   OPENAI_API_KEY=sua-chave-aqui
   ```
4. Rode o projeto:
   ```
   python3 project/app.py
   ```

A aplicação sobe em `http://localhost:5000`.

### Com Docker

1. Crie o arquivo `.env` na raiz do projeto (mesmo passo 3 acima) — ele também é usado pelo serviço `n8n`.
2. Suba os containers:
   ```
   docker compose up --build
   ```

Isso sobe dois serviços: `web` (aplicação Flask, porta `5000`) e `n8n` (automação de envio de e-mail, porta `5678`).

## Variáveis de ambiente

| Variável          | Obrigatória | Descrição                                              |
|-------------------|:-----------:|----------------------------------------------------------|
| `OPENAI_API_KEY`  | Sim         | Chave da API da OpenAI, usada em `project/classifier.py` |

## Rotas / Endpoints

| Método      | Rota      | Descrição                                                                 |
|-------------|-----------|-----------------------------------------------------------------------------|
| GET / POST  | `/`       | Formulário principal — classifica o texto colado pelo usuário               |
| POST        | `/upload` | Recebe um arquivo `.pdf` ou `.txt` e classifica seu conteúdo                |
| POST        | `/n8n`    | Recebe `{"text": "..."}` e retorna `{"Response": "..."}` — usada pelo n8n   |

## Autor

**Thalles Ribeiro Nascimento**
[LinkedIn](https://www.linkedin.com/in/thallesnascimento) · [GitHub](https://github.com/Thalles-Ribeiro-Nascimento)
