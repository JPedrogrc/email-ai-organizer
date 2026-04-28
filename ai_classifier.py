import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1" 
)

def classify_email(content: str) -> str:
    """Classifica o conteúdo de um e-mail usando IA via Groq/Llama-3."""
    # 1. TRUNCAMENTO: Pega apenas os primeiros 4000 caracteres
    content_safe = content[:4000]

    prompt = f"""
    Você é um classificador automático estrito. Analise o e-mail abaixo.
    
    Regras ABSOLUTAS:
    - Retorne EXATAMENTE as 3 linhas abaixo. 
    - Não adicione NENHUMA palavra extra, nota ou justificativa.
    - Categorias permitidas: Faculdade, Programação, Importante, Promoção/Lixo.
    
    Formato de Saída:
    Categoria: [Sua Categoria]
    Importância: [Alta, Média ou Baixa]
    Resumo: [Exatamente 1 linha resumindo]
    
    Email:
    {content_safe}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        return response.choices[0].message.content or "Erro: Resposta vazia da IA"
    except Exception as e:
        return f"Erro na IA: {e}"