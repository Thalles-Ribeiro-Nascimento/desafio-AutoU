# Categorizador de E-mails com IA

## Sobre
O categorizador de e-mails com IA é uma ferramenta web simples e eficiente para 
criar respostas automáticas conforme a categoria do e-mail. Usando a Inteligência
Artifical fazemos a classificação do e-mail em Produtivo ou Improdutivo e geramos uma
resposta automática.

## Instalação Local

### Pré-requisitos
#### Utilizar a versão 3.10 > do Python!

1 - Executar o git clone no repositório

2 - `pip install -r requirements.txt` - Instalar as dependências

3 - Criar um arquivo .env dentro do projeto para inserir a Secret_Key da OpenAI. Seguir o exemplo do
arquivo [Example.env](example.env)

4 - `python3 project/app.py` Rode o projeto. 

O projeto rodará no endereço http://localhost:5000.

[//]: # (## Acesso ao Sistema via Web)

[//]: # ()


### Ferramentas utilizadas
#### Back-end
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="100" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original-wordmark.svg" width="100"/>
                   
#### IA
OpenAI - GPT-4o-MINI

#### Front-end
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-plain-wordmark.svg" width="100"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bootstrap/bootstrap-original-wordmark.svg" width="100"/>


#### Envio de Email
N8N - Automatizando o envio de e-mail
