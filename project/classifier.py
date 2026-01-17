from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# generator_text = pipeline(
#     "text-generation",
#     model="meta-llama/Meta-Llama-3-8B-Instruct",
#     trust_remote_code=True,
#     device_map="auto"
# )
def classify_email(text):
    labels = ["Produtivo", "Improdutivo"]
    result = classifier(text, labels)
    return result["labels"][0]


def generate_response(category):
    prompt = f"""
    Você é um secretário em uma empresa Financeira
    
    Categorias:
    Produtivo: Emails que requerem uma ação ou resposta específica
     (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema)
     
     Improdutivo: Emails que não necessitam de uma ação imediata
      (ex.: mensagens de felicitações, agradecimentos).
    
    Faça uma resposta automática para o e-mail que está categorizado em {category}
    """
    text = generator_text(prompt, temperature=0.5, max_new_tokens=100, top_p=0.9)

    if category == "Produtivo":
        return text[0]['generated_text']
    else:
        return text[0]['generated_text']
