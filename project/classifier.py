from dotenv import load_dotenv
from openai import OpenAI
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
                          
                          Responda somente com 'Produtivo' ou 'Improdutivo'.
                          Emails 'promocionais' e 'diversos' categorizar como improdutivo.
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

    return category.choices[0].message.content.strip()


def generate_response(email, category):
    response = openAi.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role" : "system",
                "content" : (
                    f"""
                    Você é um assistente que responde emails de acordo com a categoria desse email.
                    Após atenciosamente usar os seguintes dados:
                    [Seu Nome] = Thalles Nascimento
                    [Seu Cargo] = Tecnologia da Informação
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
