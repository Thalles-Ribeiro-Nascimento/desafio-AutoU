from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import os

load_dotenv()

openAi = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def classify_email(text):
    category = openAi.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role" : "system",
                "content" : (
                    """
                        Você é um classificador os emails.
                
                        Categorias:
                        Produtivo: Emails que requerem uma ação ou resposta específica
                         (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema)
                
                         Improdutivo: Emails que não necessitam de uma ação imediata
                          (ex.: mensagens de felicitações, agradecimentos).
                         
                         Diversos: Emails promocionais (ex.: Ofertas, promoções, vagas, currículo)
                          
                          Responda somente com 'Produtivo', 'Improdutivo' ou 'Diversos'.
                          
                    """
                )
            },
            {
                "role" : "user",
                "content" : text
            }
        ],
        temperature=0
    )

    response_openAi = category.choices[0].message.content.strip()

    if response_openAi != "Produtivo" and response_openAi != "Improdutivo":
        return None

    return response_openAi

def generate_response(email, category):
    if category is None:
        return None

    name = os.getenv('NAME_RESPONSE')
    job = os.getenv('POSITION_RESPONSE')

    response = openAi.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role" : "system",
                "content" : (
                    f"""
                    Você é um assistente que responde emails de acordo com a categoria.
                    Não utilizar o 'Atenciosamente'. Finalizar o email dizendo que foi uma resposta automática.                    
                    Gere uma resposta clara, objetiva e simpática para o email recebido, considerando
                    a categoria '{category}'. Para categoria 'Produtivo' sua resposta precisa ser apenas automática e que 
                    o email será respondido posteriormente pelo responsável.
                    """
                )
            },
            {
                "role" : "user",
                "content" : email
            }
        ],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()

def extrair_pdf(file):
    pdf = PdfReader(file)
    text = ""

    for page in pdf.pages:
        text += page.extract_text() or ""

    return text.strip()
